import mysql.connector
from datetime import date, timedelta
import time
import requests
   
#Create the connection object
myconn = mysql.connector.connect(host = "xxxx", user = "xxxx", 
    passwd = "xxxx", database= "xxxx")
   
#printing the connection object
#print(myconn)

#sql
total_order_unknown="select count(*) from vnpt_dealer.order where created_at >= UNIX_TIMESTAMP('"+time.strftime("%Y-%m-%d")+"') and note in ('UNKNOWN','TimedOut executed,Please use check_trans function to get result.')"
print(total_order_unknown)

cursor = myconn.cursor()
cursor.execute(total_order_unknown)
result = cursor.fetchall()
for row in result:
    total_order_unknown_query=row[0]
    
body="🔹 Hệ thống ghi nhận số đơn hàng lỗi UNKNOWN: "+"*"+str(total_order_unknown_query)+"*"

print(str(total_order_unknown_query))
if int(total_order_unknown_query) > 0:
    headers = {'Content-Type': 'application/xml'} # set what your server accepts
    r = requests.post("https://api.telegram.org/bot682924377:xxxx/sendMessage?text=" + body + "&chat_id=-xxxx"+"&parse_mode=Markdown", headers=headers)
else:
   print("ok")	
