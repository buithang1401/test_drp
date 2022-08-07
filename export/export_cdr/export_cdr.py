###Lib date###
import time
import datetime
import os

###Lib Oracle###
import cx_Oracle
import csv

today = datetime.date.today()
date_start = datetime.datetime(2022, 6, 9)
date_end = datetime.datetime(2022, 7, 27)

# Database connection variable.
connect = None

dsn_tns = cx_Oracle.makedsn('xxxx', '1521', service_name='xxxx')


# File path and name.
filePath = 'H:\\CDR_SMSB\\'

# Check if the file path exists.
if os.path.exists(filePath):
    try:
        # Connect to database.
        connect = cx_Oracle.connect(user='xxxx', password='xxxx', dsn=dsn_tns,encoding="UTF-8", nencoding="UTF-8")

    except cx_Oracle.DatabaseError as e:
        # Confirm unsuccessful connection and stop program execution.
        print("Database connection unsuccessful.")
        quit()
        
    # Cursor to execute query.
    cursor = connect.cursor()
    
    try:
        while date_start < date_end:
            gen_sql = "select ID,MSISDN,SERVICE_NUMBER,MT_INFO,MO_ID,SCHEDULE_ID,STATUS,to_char(DATE_CREATE ,'YYYYMMDDHH24MISS'),to_char(DEL_TIME ,'YYYYMMDDHH24MISS'),MT_TYPE,to_char(SENT_TIME ,'YYYYMMDDHH24MISS'),TOTAL_SEGMENT,MSG_TYPE,MSC_NO,FILE_SRC from tbl_mt_log partition (tbl_mt_log_p"+str(date_start.strftime('%Y%m%d'))+")"
            print(gen_sql)
            fileName ='CDR_'+str(date_start.strftime('%Y%m%d'))+'.csv'
            print(fileName)


            f = open(filePath + fileName, "w",encoding ='utf-8')
            writer = csv.writer(f, lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
            r = cursor.execute(gen_sql)

            #this takes the column names
            col_names = [row[0] for row in cursor.description]

            print("Start export cdr "+str(date_start.strftime('%Y%m%d')))
            writer.writerow(col_names)

            for row in cursor:
                writer.writerow(row)
            f.close()
            
            # Message stating export successful.
            print("Data export successful.")

            ## increment datetime
            date_start = date_start + datetime.timedelta(1)

    except cx_Oracle.DatabaseError as e:

        # Confirm error retrieving person information and stop program execution.
        print("Error retrieving person information.")
        quit()

    finally:

        # Close database connection.
        connect.close()

else:

    # Message stating file path does not exist.
    print("File path does not exist.")