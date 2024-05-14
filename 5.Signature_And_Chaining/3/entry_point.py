
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp
from celery import group



def deposit_and_send_sms_using_group():
    bank_deposit_money(1234, 5000)
    bank_deposit_money(4321, 3000)
    bank_deposit_money(5678, 7000)

    # Create the signature for multiple tasks
    sig_sms = task_send_sms.si(1234, "Your account has been credited with $5000")
    sig_sms_1 = task_send_sms.si(4321, "Your account has been credited with $3000")
    sig_sms_2 = task_send_sms.si(5678, "Your account has been credited with $7000")

    sig_whatsapp = task_send_whatsapp.si(1234, "Your account has been credited with $5000")
    sig_whatsapp_1 = task_send_whatsapp.si(4321, "Your account has been credited with $3000")
    sig_whatsapp_2 = task_send_whatsapp.si(5678, "Your account has been credited with $7000")

    # Create the group of a signatures
    grp = group(sig_sms, sig_sms_1, sig_sms_2, sig_whatsapp, sig_whatsapp_1, sig_whatsapp_2)
    
    # Execute the group
    grp.delay()
    #or
    grp.apply_async()


if __name__ == "__main__":
    deposit_and_send_sms_using_group()

    


  


