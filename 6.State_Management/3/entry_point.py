
import time
from banking import bank_deposit_money
from task_one import states, first_action, second_action


def sm_tasks_1():
    result = first_action.delay(1)
    result.get()

def sm_tasks_2():
    result = second_action.delay(1)
    result.get()

    

if __name__ == "__main__":
    sm_tasks_1()
    sm_tasks_2()

    


  


