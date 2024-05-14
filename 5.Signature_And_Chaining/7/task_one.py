

from celery import Celery
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')

sms_sent_count = 0
whatsapp_sent_count = 0


@app.task
def task_send_sms(account_no, message):
    time.sleep(2)
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    global sms_sent_count
    sms_sent_count += 1
    return "SMS Sent Successfully.....!!!!"

@app.task
def task_send_whatsapp(sms_sent_status, account_no, message):
    time.sleep(2)    
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".format(account_no, message))
    global whatsapp_sent_count
    whatsapp_sent_count += 1
    return "WhatsApp Sent Successfully!!!!!!!"


@app.task
def total_sms_sent():
    global sms_sent_count
    return sms_sent_count   

@app.task
def total_whatsapp_sent():
    global whatsapp_sent_count
    return whatsapp_sent_count


    





