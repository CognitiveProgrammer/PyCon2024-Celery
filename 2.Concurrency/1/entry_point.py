
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp

def deposit_and_send_sms_repetatively(account_no, amount, message):
    bank_deposit_money(account_no, amount)
    # send SMS and WhatsApp
    task_send_sms.delay(account_no, message)
    task_send_whatsapp.delay(account_no, message)



if __name__ == "__main__":
    deposit_and_send_sms_repetatively(1234, 5000, "Your account has been credited with $5000")

    


  


