
from celery import Celery
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')


# senf SMS notifications to the account holder
@app.task
def task_send_sms(account_no, message):
    time.sleep(5)  # sleep for 5 seconds
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    return "SMS Sent Successfully!!!!!!!"

@app.task
def task_send_whatsapp(account_no, message):
    time.sleep(5)  # sleep for 5 seconds
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".format(account_no, message))
    return "WhatsApp Message Sent Successfully!!!!!!!"





