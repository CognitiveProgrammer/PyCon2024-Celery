
import time
from task_one import check_args_and_kwargs

def send_arguments():

    # send args and kwargs
    #check_args_and_kwargs.apply_async((1, 2, 3, 4, 5), {"name": "Daksh", "Place":  "PyCon2024" })

    # try it with delay also and spot the difference
    check_args_and_kwargs.delay((1, 2, 3, 4, 5), {"name": "Daksh", "Place":  "PyCon2024" })

if __name__ == "__main__":
    send_arguments()

    