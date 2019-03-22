import mysql.connector
import time
import re
import datetime

# GoIP API
import requests
import json
import pprint
import re

from multiprocessing import Process

# URL Encoding
import urllib



def goip_send(provider,number,message,goip):
 
    if provider == 'GLOBE':
        provider = 1
    elif provider == 'SMART':
        provider = 2
    elif provider == 'SPECIAL1':
        provider = 3
    elif provider == 'SPECIAL2':
        provider = 4
    else:
        provider = 0

    # Encode to URL Format
    message = urllib.quote_plus(message)

    # Replace Provider
    url = "http://localhost/goip/en/dosend.php?USERNAME=root&PASSWORD=root&smsprovider=" + str(provider) + "&goipname=" + goip + "&smsnum=" + number + "&method=2&Memo=" + message
    reply = requests.post(url)
    # print(reply.text)
    messageid = re.search(r'messageid=(.*?)&USERNAME',reply.text).group(1)

    send_url = "http://localhost/goip/en/resend.php?messageid=" + messageid + "&USERNAME=root&PASSWORD=root"
    send_reply = requests.post(send_url)
    # print(send_reply.text)

    if 'errorstatus' in send_reply.text:
        status = re.search(r'errorstatus:(.*)',send_reply.text).group(1)
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
        


while True:

        # print(goip)
        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        sql = "SELECT * FROM sirvasmsapp_queue WHERE flag = 0 AND provider = 'SPECIAL1';".format(id)
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:

                id = str(row[0])
                date = str(row[1])
                provider = str(row[2])
                to_number = str(row[3])
                user = str(row[4])
                message = str(row[5])
                flag = str(row[6])
                tag = str(row[7])
                # goip = str(row[8])
                goip = 'GoIPD07'

                results = goip_send(provider,to_number,message,goip)

                print(id + ' | ' + date + ' | ' + provider + ' | ' + to_number+ ' | ' + user + ' | ' + message + ' | ' + tag + ' | ' + goip + ' | ' + flag + ' | ' + str(datetime.datetime.now()))
                
                if results['status'] == 'Failed':
                    updateStatus(id,goip,2)
                elif results['status'] == 'Sent':
                    updateStatus(id,goip,1)

                # Update Which Tag is Sending SMS
                update_sending(tag)
        else:
                update_sending('Clear')


