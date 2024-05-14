
import time
from task_one import first_task, second_task, third_task


def put_task_in_respective_queues():
    first_task.delay() # default Queue

    second_task.delay() # second Queue

    third_task.delay() # third Queue
    

if __name__ == "__main__":
    put_task_in_respective_queues()

