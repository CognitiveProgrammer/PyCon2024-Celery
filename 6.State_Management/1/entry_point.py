
import time
from banking import bank_deposit_money
from task_one import bounded_task


def call_bounded_task():
    bounded_task.delay(("Daksh", "Gupta"), kwargs = {"ConfName": "PyCon2024", "place": "Pittsburgh"})
    print("Bounded Task Called")
    

if __name__ == "__main__":
    call_bounded_task()

    


  


