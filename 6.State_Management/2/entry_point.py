
import time
from banking import bank_deposit_money
from task_one import states, first_action, second_action


def sm_tasks(sm_client):
    result = first_action.delay(sm_client.to_dict())
    # print all the attributes of the sm_client
    sm_first_res = states.from_dict(result.get())
    print(sm_first_res.__dict__)
    
    result2 = second_action.delay(sm_first_res.to_dict())
    sm_second_res = states.from_dict(result2.get())
    print(sm_second_res.__dict__)

    

if __name__ == "__main__":
    sm_client = states("Client_1")
    sm_tasks(sm_client)

    


  


