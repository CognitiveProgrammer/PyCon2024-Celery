

from celery import Celery, states
import time

app = Celery('cel_main', backend='rpc://', broker='pyamqp://')


class states:
    def __init__(self, client_id):
        self.client_id = client_id
        self.available_states = ["READY", "IN_PROGRESS", "SUCCESS", "FAILURE"]
        self.curr_state = self.available_states[0]
        self.action_taken = []
        self.action_result = []

global_states = {}

@app.task
def first_action(client_id):
    sm_client = None
    if(client_id in global_states):
        sm_client = global_states[client_id]
    else:
        sm_client = states(client_id)
        global_states[client_id] = sm_client
        
    sm_client.curr_state = sm_client.available_states[1]
    print("First Action - CALLED.........!!!!!!!!!!!")
    time.sleep(2)

    # Add the result of first_action to the client_states
    sm_client.action_taken.append("first_action")
    sm_client.action_result.append("SUCCESS")
    sm_client.curr_state = sm_client.available_states[2]
    #Add logs
    sm_client.curr_state = sm_client.available_states[0]

    print(sm_client.__dict__)




@app.task
def second_action(client_id):
    sm_client = None
    if(client_id in global_states):
        sm_client = global_states[client_id]
    else:
        sm_client = states(client_id)
        global_states[client_id] = sm_client

    sm_client.curr_state = sm_client.available_states[1]
    print("2nd Action - CALLED.........!!!!!!!!!!!")
    time.sleep(2)

    # Add the result of first_action to the client_states
    sm_client.action_taken.append("second_action")
    sm_client.action_result.append("SUCCESS")
    sm_client.curr_state = sm_client.available_states[2]
    #Add logs
    sm_client.curr_state = sm_client.available_states[0]
    
    print(sm_client.__dict__)

    

@app.task
def task_send_sms(self, account_no, message):
    print("Sending SMS to account holder of {0} with message \n\n {1}".format(account_no, message))
    time.sleep(2)
    return "SMS Sent Successfully...!!!!"


@app.task
def task_send_whatsapp(sms_sent_status, account_no, message):
    print("SMS Sent Status is {0}".format(sms_sent_status))
    time.sleep(2)
    return "WhatsApp Sent Successfully...!!!!"
    





