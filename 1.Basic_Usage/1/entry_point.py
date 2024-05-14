

from banking import bank_deposit_money
from task_one import task_send_sms

# Deposit money into the bank account and send the sms
def deposit_and_send_sms(account_no, amount, message):
    bank_deposit_money(account_no, amount)
    task_send_sms(account_no, message)


if __name__ == "__main__":
    deposit_and_send_sms(1234, 5000, "Your account has been credited with $5000")
    