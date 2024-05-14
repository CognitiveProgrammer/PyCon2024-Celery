
from celery import Celery, states
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')
    

@app.task
def task_send_sms(account_no, message):
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    time.sleep(2)
    return "SMS Sent Successfully...!!!!"


@app.task
def task_send_whatsapp(account_no, message):
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".format(account_no, message))
    time.sleep(2)
    return "WhatsApp Sent Successfully...!!!!"
    





