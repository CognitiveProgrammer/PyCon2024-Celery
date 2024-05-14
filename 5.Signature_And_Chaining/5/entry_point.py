
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp
from celery import chain

def send_sms_and_whatsapp_using_chain(account_no, amount, message):
    sig_sms = task_send_sms.signature((account_no, message))
    sig_whatsapp = task_send_whatsapp.signature((account_no, message))

    #chain the signatures

    result = chain(sig_sms, sig_whatsapp).delay()
    # or
    #result = chain(sig_sms, sig_whatsapp).apply_async()
    
    print(result.get())


if __name__ == "__main__":
    send_sms_and_whatsapp_using_chain(12345, 1000, "Hello, Your account has been credited with 5000 USD")

    


  


