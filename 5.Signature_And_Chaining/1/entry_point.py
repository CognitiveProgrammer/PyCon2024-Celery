
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp


def deposit_and_send_sms_using_signature(account_no, amount, message):
    bank_deposit_money(account_no, amount)
    # Create the signature
    sig_sms = task_send_sms.si(account_no, message)

    # Apply the signature
    sms_sent_status = sig_sms.delay()
    # or
    sms_sent_status = sig_sms.apply_async()
    #or
    sms_sent_status = sig_sms.apply_async(countdown=5)
  

if __name__ == "__main__":
    deposit_and_send_sms_using_signature(1234, 5000, "Your account has been credited with $5000")

    


  


