from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp

# Deposit money into the bank account and send the sms & whatsapp
def deposit_and_send_sms(account_no, amount, message):
    bank_deposit_money(account_no, amount)
    # send SMS and WhatsApp
    
    sms_sent_status = task_send_sms.delay(account_no, message)
    whatsapp_sent_status = task_send_whatsapp.delay(account_no, message)

    print("SMS Status: ", sms_sent_status.get())
    print("WhatsApp Status: ", whatsapp_sent_status.get())
    

if __name__ == "__main__":
    deposit_and_send_sms(1234, 5000, "Your account has been credited with $5000")


  


