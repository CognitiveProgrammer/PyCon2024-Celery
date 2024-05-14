
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp
from celery import group

def send_sms_and_whatsapp_using_linking(account_no, amount, message):
    sig_sms = task_send_sms.s(account_no, message)
    sig_whatsapp = task_send_whatsapp.s(account_no, message)

    grp = group(sig_whatsapp,sig_sms)

    grp_result = grp.delay()
    # or
    grp_result = grp.apply_async()

    print(grp_result.get())

if __name__ == "__main__":
    send_sms_and_whatsapp_using_linking(12345, 1000, "Hello, Your account has been credited with 5000 USD")

    


  


