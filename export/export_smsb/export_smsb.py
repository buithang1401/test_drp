#Code by Anhln
#Time Create: 26/06/2021
#name: import_redis
#select REPLACE(REPLACE(REPLACE(NAME,'/','_'),',','_'),' ','_'),to_char(TIME_SEND,'yyyymmdd'),id from tbl_schedule where name in 
#E:\VNTP_VAS\Media-Vas\source\python\export_smsb

import datetime
import time
import shutil
import os

###Lib Oracle###
import cx_Oracle
import csv


def Export_Campagin_Smsb():

            strListFolder = 'E:\\python\\export_smsb\\'

            print ("---> START read file: \n")
            arrFile = os.listdir(strListFolder)
            dsn_tns = cx_Oracle.makedsn('xxxx', '1521', service_name='xxxx')
            connect = cx_Oracle.connect(user='xxxx', password='xxxx', dsn=dsn_tns)
            cursor = connect.cursor()
            for i in arrFile:
                if (i.endswith('.txt')):
                    print ("read file: " + i + "\n")
                    fread= open(strListFolder + "/" + i,'r')
                    linesReads = fread.readlines();
                    for lineRead in linesReads:
                        lineRead = lineRead.replace("\n","")
                        arrayInfo = lineRead.split(",")
                        Schedule_Name =  arrayInfo[0]
                        date_export = arrayInfo[1]
                        Schedule_Id = arrayInfo[2]
                        gen_sql="select distinct msisdn from tbl_mt_log partition (tbl_mt_log_p"+date_export+") where SCHEDULE_ID = '"+Schedule_Id+"' and status = '0'"+""" and msisdn not in 
                                ('84888434xxx','84888434xxx')"""
                        print(gen_sql)
                        cursor.execute(gen_sql)
                        results = cursor.fetchall()
                        textFile = csv.writer(open('E:\\python\\export_smsb\\' + Schedule_Id+'_'+Schedule_Name + '.csv', 'w', newline=''),
                              delimiter=',', lineterminator='\r\n',
                              quoting=csv.QUOTE_NONE, escapechar='\\')
                        textFile.writerows(results)

                    fread.close()
Export_Campagin_Smsb()