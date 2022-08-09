#!/usr/bin/python
# -*- coding: utf8 -*-

import cx_Oracle
import xlwt
#import datetime
from datetime import date, timedelta
import time

###Lib smpp###
import smtplib
import os.path as op
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

 
yesterday=date.today() - timedelta(1) 
filename = 'report_don_hang_tra_truoc_'+time.strftime("%Y-%m-%d")+'.xls'
out_path = '/home/media/scripts/report_don_hang_tra_truoc/report_don_hang_tra_truoc_'+time.strftime("%Y-%m-%d")+'.xls'
print(out_path)
 
sheet01 = 'report'+time.strftime("%Y-%m-%d")
#Get the data whose release time and system time are the same month
sql01="""select a.PACKAGE_ID,a.PACKAGE_CODE, a.AGENT_ID, b.agent_name, to_char(a.CREATED_DATE,'YYYY-MM-DD HH24:MI:SS') as CREATED_DATE, 
to_char(a.DESTROYED_DATE,'YYYY-MM-DD HH24:MI:SS') as DESTROYED_DATE, to_char(a.EXPIRED_DATE,'YYYY-MM-DD HH24:MI:SS') as EXPIRED_DATE, 
a.PRICE, decode(a.contract_type_id,1,'CSKH',2,'QC','Khac')  as CONTRACT_TYPE, c.label_type_name, decode(a.STATUS, 0, 'Dừng', 1, 'Hoạt Động') as STATUS, a.LIMIT,a.SEND_NUMBER, 
ROUND(a.SEND_NUMBER/a.LIMIT*100,0) As "% USE"
from agent_package a, agent b, label_type c where nvl(a.ads_type_id,0) <> 2 
and a.EXPIRED_DATE > TRUNC(ADD_MONTHS(SYSDATE, -1),'MM') and a.CREATED_USER = 'approve'
and a.agent_id = b.agent_id
and c.telco_id = 1
and c.agent_type = b.agent_type
and c.contract_type_id = a.contract_type_id
and a.label_type = c.label_type_id
-- and c.agent_type = 0
and a.status in (0,1)
order by LIMIT desc"""
 
workbook = xlwt.Workbook(encoding ='utf-8') # workbook is the carrier on which sheet depends.
def main(sql,sheet,sheet_name):
     #conn = cx_Oracle.connect("user/passwd@ip/sid")
     dsn_tns = cx_Oracle.makedsn('xxxx', '1521', service_name='xxxx')
     conn = cx_Oracle.Connection('xxxx','xxxx',dsn_tns,encoding="UTF-8", nencoding="UTF-8")
     cursor =conn.cursor()
     result = cursor.execute(sql)
      
     #Search all results
     results = cursor.fetchall()
     # Get the data field name in MYSQL
     fields = cursor.description
     sheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)
     # Write field information
     for field in range(0,len(fields)):
          sheet.write(0,field,fields[field][0])
         # Get and write data segment information
     row = 1
     col = 0
     for row in range(1,len(results)+1):
          for col in range(0,len(fields)):
               sheet.write(row,col,u'%s'%results[row-1][col])
     workbook.save(out_path)
 
 
####Email##
def send_mail(send_from, send_to, subject, message, files=[],
              server="localhost", port=587, username='', password='',
               use_tls=True):
     """Compose and send email with provided info and attachments.

     Args:
        send_from (str): from name
        send_to (str): to name
        subject (str): message title
        message (str): message body
        files (list[str]): list of file paths to be attached to email
        server (str): mail server host name
        port (int): port number
        username (str): server auth username
        password (str): server auth password
        use_tls (bool): use TLS mode
     """
     msg = MIMEMultipart()
     msg['From'] = send_from
     msg['To'] = COMMASPACE.join(send_to)
     msg['Date'] = formatdate(localtime=True)
     msg['Subject'] = subject

     msg.attach(MIMEText(message))

     for path in files:
          part = MIMEBase('application', "octet-stream")
          with open(path, 'rb') as file:
               part.set_payload(file.read())
          encoders.encode_base64(part)
          part.add_header('Content-Disposition',
                        'attachment; filename="{}"'.format(op.basename(path)))
          msg.attach(part)

     smtp = smtplib.SMTP(server, port)
     if use_tls:
          smtp.starttls()
     smtp.login(username, password)
     smtp.sendmail(send_from, send_to, msg.as_string())
     smtp.quit()
  
if __name__ == '__main__': 
     main(sql01,sheet01,sheet01)
     ##Body
     localtime = time.asctime( time.localtime(time.time()) )
     Line1 = "File report Đơn hàng trả trước ngày: " + time.strftime("%Y-%m-%d")
     Body = Line1
     send_mail('xxx@xxxx.vn', ['xxxx@xxxx.vn','xxxx@xxxx.vn'], '[xxxx] File report Đơn hàng trả trước', Body, [out_path],'email.xxxx.vn',587,'xxxx@xxxx.vn','xxxx','True')
