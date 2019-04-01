import mysql.connector
import time
import re
import datetime

# GoIP API
import requests
import json
import pprint
import re

from multiprocessing import Process, current_process

# URL Encoding
import urllib


def goip_send(provider,number,message,goip):
 
    if provider == 'GLOBE':
        provider = 1
    elif provider == 'SMART':
        provider = 2
    elif provider == 'SPECIAL01':
        provider = 3
    elif provider == 'SECIAL02':
        provider = 4
    else:
        provider = 0

    # ENCODE MESSAGE TO URL FORMAT
    message = urllib.quote_plus(message)

    # FORMAT SENDING URL
    url = "http://localhost/goip/en/dosend.php?USERNAME=root&PASSWORD=root&smsprovider=" + str(provider) + "&goipname=" + goip + "&smsnum=" + number + "&method=2&Memo=" + message
    reply = requests.post(url)
    # print(reply.text)
    messageid = re.search(r'messageid=(.*?)&USERNAME',reply.text).group(1)

    # FORCE TO SEND SMS
    send_url = "http://localhost/goip/en/resend.php?messageid=" + messageid + "&USERNAME=root&PASSWORD=root"
    send_reply = requests.post(send_url)
    # print(send_reply.text)

    if 'errorstatus' in send_reply.text:
        status = 'Failed'
    elif 'ok(' in send_reply.text:
        status = 'Sent'
    else:
        status = 'Failed'

    return {'messageid':messageid,'status':status}

def update_sending(tag):

        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        sql = "UPDATE sirvasmsapp_queueblast SET status = 'Finish'"
        cursor.execute(sql)
        conn.commit()
        conn.close()

        if tag != 'Clear':

                conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
                cursor = conn.cursor()
                sql = "UPDATE sirvasmsapp_queueblast SET status = 'Sending' WHERE tag = '{}'".format(tag)
                cursor.execute(sql)
                conn.commit()
                conn.close()

def updateStatus(_id,goip,status):

        now = datetime.datetime.now()
  
        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        sql = "UPDATE sirvasmsapp_queue SET dateSent = '{}', goip = '{}', flag = '{}' WHERE id = '{}'".format(now,goip,status,_id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        
def onlineGoIP():

        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        # sql = "SELECT goip.name FROM goip WHERE (alive = 1 AND gsm_status = 'LOGIN' AND provider = 1) OR  (alive = 1 AND gsm_status = 'LOGIN' AND provider = 2) ORDER BY name ASC;" 
        sql = "SELECT goip.name FROM goip WHERE (alive = 0 AND gsm_status = '' AND provider = 1) OR  (alive = 0 AND gsm_status = '' AND provider = 2) ORDER BY name ASC;" 
        cursor.execute(sql)
        result = cursor.fetchall()

        onlineGoIP = []

        for row in result:
            onlineGoIP.append(row[0])

        return(onlineGoIP)

def getQueues():

    onlineGoIPList = onlineGoIP()

    # GET ALL MESSAGES ON QUEUE
    conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
    cursor = conn.cursor()
    sql = "SELECT * FROM sirvasmsapp_queue WHERE flag = 0 AND provider NOT LIKE 'SPECIAL%';" 
    cursor.execute(sql)
    result = cursor.fetchall()

    # QUEUE ASSIGNMENT TO GOIP
    QueueLists = [] 

    # COUNT TOTAL ONLINE GOIP
    onlineGoIPTotal = len(onlineGoIPList) - 1
    # SET GOIP COUNT 0
    onlineGoIPCount = 0

    for row in result:

        # RESET THE CYCLE
        if onlineGoIPCount > onlineGoIPTotal:
            onlineGoIPCount = 0

        # SET ID
        id = row[0] 
        # GET ASSIGN GOIP
        goip = onlineGoIPList[onlineGoIPCount]
        # ASSIGN NEXT GOIP
        onlineGoIPCount = onlineGoIPCount + 1
        # APPEND TO LIST
        QueueLists.append({'id':id,'goip':goip})

    return QueueLists

def processMessage(goip):


        while True:

            # GET ALL SMS ON QUEUE THEN CREATE A LIST
            QueueLists = getQueues()

            # IF QUEUE LIST HAS ITEM
            if QueueLists:
                
                # GET THE INDEX BASE ON GOIP NAME
                queue_index = next((index for (index, d) in enumerate(QueueLists) if d["goip"] == goip), None)
                # IF GOIP NAME IS ON THE LIST
                if queue_index is not None:
                    # GET QUEUE SMS ID
                    id = QueueLists[queue_index]['id']
                    # REMOVE FROM THE LIST
                    QueueLists.pop(queue_index)
                    # GET ONE RECORD FROM QUEUE
                    conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
                    cursor = conn.cursor()
                    sql = "SELECT * FROM sirvasmsapp_queue WHERE id = '{}';".format(id)
                    cursor.execute(sql)
                    row = cursor.fetchone()

                    if row: # READ THE RECORD
                            id = str(row[0])
                            date = str(row[1])
                            provider = str(row[2])
                            to_number = str(row[3])
                            user = str(row[4])
                            message = str(row[5])
                            flag = str(row[6])
                            tag = str(row[7])
                            # UPDATE RECORD QUEUE STATUS
                            updateStatus(id,goip,3)
                            # CALL SMS API
                            results = goip_send(provider,to_number,message,goip)
                            print(id + ' | ' + date + ' | ' + provider + ' | ' + to_number+ ' | ' + user + ' | ' + message[:15] + ' | ' + tag + ' | ' + goip + ' | ' + flag + ' | ' + str(datetime.datetime.now()))
                            
                            # UPDATE QUEUE STATUS
                            if results['status'] == 'Failed':
                                updateStatus(id,goip,2)
                            elif results['status'] == 'Sent':
                                updateStatus(id,goip,1)

                            # UPDATE WHICH TAG IS SENDING
                            update_sending(tag)

                    else:
                            update_sending('Clear')


###########################################################################################################
# PROCESS START HERE!
###########################################################################################################


# GET ONLINE GOIP LISTS
onlinegoip = onlineGoIP()

# PROCESS LISTS
procceses = []

# SET ZERO COUNTER
count = 0

for goip in onlinegoip:
    process = Process(target=processMessage, args=(goip,))
    procceses.append(process)
    process.start()
    count = count + 1
    
















