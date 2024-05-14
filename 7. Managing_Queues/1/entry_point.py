
import time
from banking import bank_deposit_money
from task_one import states, task_send_sms, task_send_whatsapp


def put_task_in_first_queue():
    result = task_send_sms.apply_async((12345, "USD $5000 Deposited"), queue="first")
    print(result.get())

def put_task_in_second_queue():
    result = task_send_whatsapp.apply_async((12345, "USD $5000 Deposited"), queue="second")
    print(result.get())
    

if __name__ == "__main__":
    put_task_in_first_queue()
    put_task_in_second_queue()
