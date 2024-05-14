
from celery import Celery, states
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')


@app.task(bind=True)
def bounded_task(self, *args, **kwargs):
    print(">>>>>>>>>>>>>>>----------------->>>>>>>>>>>>>>>>")
    # print the task id
    print("Task ID: {0}".format(self.request.id))
    # print the task name
    print("Task Name: {0}".format(self.name))
    # print the task args
    print("Task Args: {0}".format(self.request.args))
    # print the task kwargs
    print("Task Kwargs: {0}".format(self.request.kwargs))
    # print the task status
    print("Task Status: {0}".format(self.AsyncResult(self.request.id).state))
    print(">>>>>>>>>>>------------------>>>>>>>>>>>>>>>>>>>>")


@app.task
def task_send_sms(self, account_no, message):
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    time.sleep(2)
    return "SMS Sent Successfully...!!!!"


@app.task
def task_send_whatsapp(sms_sent_status, account_no, message):
    print("SMS Sent Status is {0}".format(sms_sent_status))
    time.sleep(2)
    return "WhatsApp Sent Successfully...!!!!"
    





