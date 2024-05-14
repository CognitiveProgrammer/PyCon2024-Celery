import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp
from celery import group

'''
Grouping tasks together
Can be used for parallel execution of the tasks
'''

def deposit_and_send_sms_whatsapp_using_group():
    bank_deposit_money(1234, 5000)

    sig_sms = task_send_sms.s(4321, "Your account has been credited with $5000")
    sig_whatsapp = task_send_whatsapp.s(4321, "Your account has been credited with $5000")

    grp = group(sig_sms, sig_whatsapp)

    grp.delay()
    #or
    grp.apply_async()
    #or
    grp.apply_async(countdown=5)



if __name__ == "__main__":
    deposit_and_send_sms_whatsapp_using_group()


    


  


