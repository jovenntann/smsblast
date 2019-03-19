import mysql.connector
import time
import datetime
import re

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




