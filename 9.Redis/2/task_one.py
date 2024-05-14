

from celery import Celery
import time

app = Celery('task_one', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')


@app.task
def task_send_sms(account_no, message):
    time.sleep(2)
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    return "SMS Sent Successfully.....!!!!"

@app.task
def task_send_whatsapp(account_no, message):
    time.sleep(2)    
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".format(account_no, message))
    return "WhatsApp Sent Successfully!!!!!!!"


@app.task
def total_sms_sent():
    time.sleep(3)  
    return 2   

@app.task
def total_whatsapp_sent():
    time.sleep(3)  
    return 2

@app.task
def get_the_result(result):
    print("Result is => ",result)
    return result
    





