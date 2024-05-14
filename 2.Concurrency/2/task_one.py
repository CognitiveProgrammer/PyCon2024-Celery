

from celery import Celery
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')

# send SMS notifications to the account holder
@app.task
def task_send_sms(account_no, message):
    time.sleep(1)
    print("Sending SMS to account holder of {0} with message \n\n {1}".
            format(account_no, message))

@app.task
def task_send_whatsapp(account_no, message):
    time.sleep(5)
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".
    format(account_no, message))



