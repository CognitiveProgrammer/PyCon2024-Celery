
from celery import Celery

# senf SMS notifications to the account holder
def task_send_sms(account_no, message):
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))

