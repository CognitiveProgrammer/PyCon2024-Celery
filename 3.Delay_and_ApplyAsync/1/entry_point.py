
import time
from banking import bank_deposit_money
from task_one import task_send_sms, task_send_whatsapp

def trigger_delayed_notifications(account_no, amount, message):
    bank_deposit_money(account_no, amount)

    # send SMS and WhatsApp delayed
    task_send_sms.apply_async((account_no, message), countdown=5)
    
    task_send_whatsapp.apply_async((account_no, message), countdown=5)


if __name__ == "__main__":
    trigger_delayed_notifications(1234, 5000, "Your account has been credited with $5000")

    