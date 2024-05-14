import celery
from celery import Celery
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')

#app.conf.task_default_queue = "first"


@app.task (queue='second')
def second_task():
    print("Second Task - CALLED")
    print("Second Task - DONE")
    return "Second Task Done."

@app.task (queue='third')
def third_task():
    print("Third Task - CALLED")
    print("Third Task - DONE")
    return "Third Task Done."

@app.task(queue='first')
def first_task():
    print("First Task - CALLED")
    print("First Task - DONE")
    return "First Task Done."



