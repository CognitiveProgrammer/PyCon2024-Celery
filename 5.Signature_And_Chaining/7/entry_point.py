
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp, total_sms_sent, total_whatsapp_sent
from celery import chord, group

def send_sms_and_whatsapp_using_chain(account_no, amount, message):
    # group 1 to sent message
    sig_sms = task_send_sms.signature((account_no, message))
    sig_whatsapp = task_send_whatsapp.signature((account_no, message))

    group_msg_send = group(sig_sms, sig_whatsapp)
    
    # group 2 to count the number of messages sent
    sig_sms_count = total_sms_sent.signature()
    sig_whatsapp_count = total_whatsapp_sent.signature()

    group_msg_status = group(sig_sms_count, sig_whatsapp_count)

    # create a chord with the two groups
    chord_result = chord(group_msg_send, group_msg_status)

    result = chord_result.delay()
    
    print("Result: ", result.get())


if __name__ == "__main__":
    send_sms_and_whatsapp_using_chain(12345, 1000, "Hello, Your account has been credited with 5000 USD")

    


  


