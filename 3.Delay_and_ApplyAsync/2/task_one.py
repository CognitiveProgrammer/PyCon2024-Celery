

from celery import Celery
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')

# arguments and Keyword arguments

@app.task
def check_args_and_kwargs(*args, **kwargs):
    print("Arguments: ", args)
    print("Keyword Arguments: ", kwargs)

    print("Arguments and Keyword Arguments Received Successfully!!!!")


# senf SMS notifications to the account holder
@app.task
def task_send_sms(account_no, message):
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))

@app.task
def task_send_whatsapp(account_no, message):
    print("Sending WhatsApp to account holder of {0} with message \n\n {1}".format(account_no, message))

