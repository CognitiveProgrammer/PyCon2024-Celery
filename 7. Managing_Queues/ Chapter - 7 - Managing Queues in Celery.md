## Chapter - 7 : Managing Queues in Celery

_The broker `RabbitMQ` is all about queues and is capable of having more than one queues, just like any other message broker out there_
_one queue is hardly sufficient for any production level software_
<br/>

_It may be possible that we want to separate out queues for various tasks in celery for reasons including not limited to better management, load balancing and security and the good news is that we can create multiple queues in `celery` and corresponding queues in `RabbitMQ` handle different different tasks in different queue_

<br/>

#### But what we're doing till now? Which Queue was that?

_The default queue name is `Celery`, which we're using all the time_
<br/>

_Here is the command to check all the active queues in the celery_

```
celery -A task_one inspect active_queues
```

<br/><br/>

#### Creating named queues in Celery

_We can create named queues in celery while instantiating the workers_

```
celery -A task_one worker --loglevel=INFO -Q first
```
_We can create multiple queues by giving a comma separated queue names_

```
celery -A task_one worker --loglevel=INFO -Q first,second,third
```

_we can also see the same in the `RabbitMQ` Dashboard_


![Task In Queue](queue2.png)

#### Submitting a task in a particular queue

_We can use the `apply_async` to put a task in particular queue. For example, if we want to put a task in a queue name first, here is how we're going to call the function_

![Task In Queue](queue1.png)

<br>
<h4>Example : 1</h4>
<br/>

#### Changing the Default Queue of the Celery Tasks

_When we created workers by specifying the queue name, the default queue named `celery` no longer exists. In this case we need to explicitly mention the name of a queue while calling a task_
<br/>

_in the example above, if we remove the name of the queue in the  `task_send_sms` or `task_send_whatsapp` then the task will not be executed_

```
result = task\_send\_sms.apply\_async((12345, "USD $5000 Deposited"))

```
<br>
<h4>Example : 2</h4>
<br/>


<br/>

_By default a queue name `Celery` is created and the serves as a default queue. However, when we create named queues then we need to decide on which one is the default so that all the tasks where the queue name is not mentioned or called using `delay` can be forwarded to the default queue_

![Task In Queue](queue3.png)


#### Task Routing in Celery

_We can create manual routes in celery and we can do the same by providing the queue parameter in the `app.Task` method. In the example below, we've created 3 queues_

```
celery -A task_one worker --loglevel=INFO -Q first,second,third
```
![Queue With Routers](queue4.png)
<br>
<h4>Example : 3</h4>
<br/>


