#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import mysql.connector as mysql
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import json

# Enable logging
#logging.basicConfig(
#    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
#)

# Enable Loging INFO/DEBUG
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


logger = logging.getLogger(__name__)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


user_name = 'testuser'
password = '123465422'

def order(update, context):
    try:
        '''
        number1 = int(context.args[0])
        #number2 = int(context.args[1])
        #result = number1+number2
        conn = mysql.connect(host='xxxx', database='xxxx', user='xxxx', password='xxxx')
        cursor = conn.cursor()
        sql = "update vnpt_dealer.order set status = 1 where id ="+str(number1)
        print(sql)
        cursor.execute(sql)
        conn.commit()

        '''

        
        try:
            conn = mysql.connect(host='xxxx', database='xxxx', user='xxxx', password='xxxx')
            if conn.is_connected():
                cursor = conn.cursor()
                for i in context.args:
                    sql = "update vnpt_dealer.order set status = 1 where id ="+str(i)
                    print(sql)
                    cursor.execute(sql)
                    print("Record updated")
                     # the connection is not auto committed by default, so we must commit to save our changes
                    conn.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
        

        update.message.reply_text('Đã update '+str(len(context.args))+' đơn hàng sang trạng thái thành công')
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')
        
def order_simso(update, context):
    try:
        '''
        number1 = int(context.args[0])
        #number2 = int(context.args[1])
        #result = number1+number2
        conn = mysql.connect(host='xxxx', database='xxxx', user='xxxx', password='xxxx')
        cursor = conn.cursor()
        sql = "update vnpt_dealer.order set status = 1 where id ="+str(number1)
        print(sql)
        cursor.execute(sql)
        conn.commit()

        '''

        
        try:
            conn = mysql.connect(host='xxxx', database='xxxx', user='xxxx', password='xxxx')
            if conn.is_connected():
                cursor = conn.cursor()
                for i in context.args:
                    sql = "update vnpt_dealer.order set status = 17 where id ="+str(i)
                    print(sql)
                    cursor.execute(sql)
                    print("Record updated")
                     # the connection is not auto committed by default, so we must commit to save our changes
                    conn.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
        

        update.message.reply_text('Đã update '+str(len(context.args))+' đơn hàng sang trạng thái cho phép kích hoạt sim hộ')
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')

def ctv_xacthuc(update, context):
    try:
        '''
        number1 = int(context.args[0])
        #number2 = int(context.args[1])
        #result = number1+number2
        conn = mysql.connect(host='xxxx', database='xxxx', user='xxxx', password='xxxx')
        cursor = conn.cursor()
        sql = "update user set status = 2 where status <> 5 and phone_number = '"+str(number1)+"'"
        print(sql)
        cursor.execute(sql)
        conn.commit()

        '''

        
        try:
            conn = mysql.connect(host='xxxx', database='xxxx', user='xxxx', password='xxxx')
            if conn.is_connected():
                cursor = conn.cursor()
                for i in context.args:
                    sql = "update user set status = 2 where status <> 5 and phone_number = '"+str(i)+"'"
                    print(sql)
                    cursor.execute(sql)
                    print("Record updated")
                     # the connection is not auto committed by default, so we must commit to save our changes
                    conn.commit()
        except Error as e:
            print("Error while connecting to MySQL", e)
        

        update.message.reply_text('Đã update '+str(len(context.args))+' ctv sang trạng thái xác thực')
    except (IndexError, ValueError):
        update.message.reply_text('There are not enough numbers')

def deploy_digital_shop(update, context):
    os.system('sh /opt/apps/digital_shop/api/deploy_digital_shop.sh')
    update.message.reply_text('Đã auto deploy module digital shop trên stg')
    

def log_full(update, context):
    with open("/opt/apps/digital_shop/logs/full/full.log", "rb") as file:
        context.bot.send_document(chat_id=update.effective_chat.id, document=file,  
          filename='full.log')

def log_error(update, context):
    with open("/opt/apps/digital_shop/logs/error/error.log", "rb") as file:
        context.bot.send_document(chat_id=update.effective_chat.id, document=file,
          filename='error.log')

def log_test(update, context):
    with open("/opt/apps/digital_shop/logs/full/full.tar.gz", "rb") as file:
        context.bot.send_document(chat_id=update.effective_chat.id, document=file,
          filename='full.tar.gz')

def order_brcd(update, context):
    r = requests.get('http://127.0.0.1:5000/order_brcd?id='+str(context.args[0]))
    data = r.json()
    print(data)
    update.message.reply_text(str(data))

def order_brcd_status(update, context):
    url = "http://xxxx:8088/mediagw/g/fiber/request_status"
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': 'xxxx'}
    params = {"tinh_id":str(context.args[0]),"ds_donhang":str(context.args[1])}
    print(params)
    body = json.dumps(params)
    resp = requests.post(url=url, headers=headers, data=body, verify=False)
    resp.encoding='utf-8-sig'
    data = resp.json() #
    update.message.reply_text(str(data))


def main():
    
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("682924377:xxxx", use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("order", order))
    dp.add_handler(CommandHandler("order_simso", order_simso))
    dp.add_handler(CommandHandler("ctv_xacthuc", ctv_xacthuc))
    dp.add_handler(CommandHandler("deploy_digital_shop", deploy_digital_shop))
    dp.add_handler(CommandHandler("log_full", log_full))
    dp.add_handler(CommandHandler("log_error", log_error))
    dp.add_handler(CommandHandler("log_test", log_test))
    dp.add_handler(CommandHandler("order_brcd", order_brcd))
    dp.add_handler(CommandHandler("order_brcd_status", order_brcd_status))
   
    # log all errors
    dp.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
