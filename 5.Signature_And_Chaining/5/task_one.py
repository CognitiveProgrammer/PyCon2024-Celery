

from celery import Celery
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')


# senf SMS notifications to the account holder
@app.task
def task_send_sms(account_no, message):
    time.sleep(2)
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    return True


@app.task
def task_send_whatsapp(sms_sent_status, account_no, message):
    print("SMS Sent Status is {0}".format(sms_sent_status))
    time.sleep(2)
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".format(account_no, message))
    return "WhatsApp Sent Successfully!!!!!!!"
    
    





