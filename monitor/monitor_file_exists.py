import os.path
import requests
from shutil import copyfile
from datetime import date, timedelta

dayrm1=(date.today() - timedelta(1)).strftime("%Y%m%d")
dayrm2=(date.today() - timedelta(2)).strftime("%Y%m%d")

employee_info_path="/home/xxxx/employee_info/"
employee_info_tmp_path="/tmp/xxxx/employee_info/"
employee_info_fname="DULIEU_DIABAN_"+dayrm1+".csv"
employee_info_rm_fname="DULIEU_DIABAN_"+dayrm2+".csv"


if os.path.isfile(employee_info_tmp_path+employee_info_rm_fname):
    os.remove(employee_info_tmp_path+employee_info_rm_fname)

if os.path.isfile(employee_info_path+employee_info_fname):
        print(employee_info_fname+" file exists")
               
        src=employee_info_path+employee_info_fname
        dst=employee_info_tmp_path+employee_info_fname
        copyfile(src, dst)
else:
        message="SmartDealer "+employee_info_fname+" file not exists"
        print(message)
        headers = {'Content-Type': 'application/xml'} # set what your server accepts
        r=requests.post("https://api.telegram.org/bot682924377:xxxx/sendMessage?text="+message+" @Anhln12"+"&chat_id=-xxxx", headers=headers)

