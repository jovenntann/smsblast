import mysql.connector
import time
import datetime
import re

# GoIP API
import requests
import json
import pprint
import re

# URL Encoding
import urllib

def goip_send(number,message,provider,goip):
 
    message = urllib.quote_plus(message)
    print(message)

    url = "http://localhost/goip/en/dosend.php?USERNAME=root&PASSWORD=root&smsprovider=" + str(provider) + "&goipname=" + goip + "&smsnum=" + number + "&method=2&Memo=" + str(message)
    reply = requests.post(url)
    messageid = re.search(r'messageid=(.*?)&USERNAME',reply.text).group(1)

    send_url = "http://localhost/goip/en/resend.php?messageid=" + messageid + "&USERNAME=root&PASSWORD=root"
    send_reply = requests.post(send_url)

    if 'errorstatus' in send_reply.text:
        status = re.search(r'errorstatus:(.*)',send_reply.text).group(1)
        status = 'Failed'
    elif 'ok(' in send_reply.text:
        status = 'Sent'
    else:
        status = 'Failed'

    return {'messageid':messageid,'status':status}

def insertSMS(date, from_number, to_number, message, MessageSid, status):

        from_number = from_number.replace('+639','09')
        name = getName(from_number)
  
        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()

        sql = "INSERT INTO sirvasmsapp_received (id, date, from_number, name, to_number, message, MessageSid, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, ('AUTO', date, from_number, name, to_number, message, MessageSid, status))
        conn.commit()
        conn.close()
        
def updateStatus(_id,status):
  
        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        sql = "UPDATE receive SET flag = '{}' WHERE id = '{}'".format(status,_id)
        cursor.execute(sql)
        conn.commit()
        conn.close()
        
def getName(number):


        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        sql = "SELECT name FROM sirvasmsapp_contact WHERE number = '{}' LIMIT 1;" .format(number)
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:
                return row[0]
        else:
                return number
        


while True:

        conn = mysql.connector.Connect(host='localhost',user='root',password='09106850351',database='goip')
        cursor = conn.cursor()
        sql = "SELECT * FROM receive WHERE flag = '0' LIMIT 1;" 
        cursor.execute(sql)
        row = cursor.fetchone()

        if row:

                _id = str(row[0])
                srcnum = str(row[1])
                msg = row[3].encode('ascii', 'ignore').decode('ascii')
                date = str(row[4])
                to_number = str(row[6])
                msg = re.sub(r'.*] ', '', msg)

                print(_id + ' | ' + date + ' | ' + srcnum + ' | ' + msg)

                insertSMS(date, srcnum, to_number, msg, _id, 'Received')
                updateStatus(_id,1)



                # Forward SMS if to Special Number
                srcnum = srcnum.replace('+639','09')
                name = getName(srcnum)
                
                if to_number == 'GoIPD07':
                        forward_to = ['09331707870','09062131607']
                        count = 0
                        for i in forward_to:         
                                results = goip_send(i,"From: " + str(srcnum) + "\nName: " + name + "\n\n" + msg,3,'GoIPD07')
                                count = count + 1
                                print(results)
                elif to_number == 'GoIPD08':
                        forward_to = ['09331707870','09062131607']
                        count = 0
                        for i in forward_to:         
                                results = goip_send(i,"From: " + str(srcnum) + "\nName: " + name + "\n\n" + msg,4,'GoIPD08')
                                count = count + 1
                                print(results)



