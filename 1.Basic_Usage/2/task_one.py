
from celery import Celery

app = Celery('task_one', backend='rpc://', broker='pyamqp://guest:guest@localhost//')


# senf SMS notifications to the account holder
@app.task
def task_send_sms(account_no, message):
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))


