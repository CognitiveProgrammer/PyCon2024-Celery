
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

    # for JSON serialization and deserialization
    def to_dict(self):
        return {
            'client_id': self.client_id,
            'available_states': self.available_states,
            'curr_state': self.curr_state,
            'action_taken': self.action_taken,    
            'action_result': self.action_result,                                
        }

    @classmethod
    def from_dict(cls, data):
        sm_clinet =  cls(data['client_id'])
        sm_clinet.available_states = data['available_states']
        sm_clinet.state = data['curr_state']
        sm_clinet.action_taken = data['action_taken']
        sm_clinet.action_result = data['action_result']
        return sm_clinet


@app.task
def first_action(client_states):
    sm_client = states.from_dict(client_states)
    sm_client.curr_state = sm_client.available_states[1]
    print("First Action - CALLED.........!!!!!!!!!!!")
    time.sleep(2)

    # Add the result of first_action to the client_states
    sm_client.action_taken.append("first_action")
    sm_client.action_result.append("SUCCESS")
    sm_client.curr_state = sm_client.available_states[2]
    #Add logs
    sm_client.curr_state = sm_client.available_states[0]
    return sm_client.to_dict()



@app.task
def second_action(client_states):
    sm_client = states.from_dict(client_states)
    sm_client.curr_state = sm_client.available_states[1]
    print("2nd Action - CALLED.........!!!!!!!!!!!")
    time.sleep(2)

    # Add the result of first_action to the client_states
    sm_client.action_taken.append("second_action")
    sm_client.action_result.append("SUCCESS")
    sm_client.curr_state = sm_client.available_states[2]
    #Add logs
    sm_client.curr_state = sm_client.available_states[0]
    return sm_client.to_dict()

    

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
    





