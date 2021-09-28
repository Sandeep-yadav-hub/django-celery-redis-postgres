import time

from celery import shared_task

# @shared_task
# def create_task(task_type):
#     time.sleep(int(task_type) * 10)
#     return True

@shared_task
def add(a,b):
    time.sleep(int(2) * 10)
    return a+b
    
@shared_task
def printing(email):
    print(f'Sent mail to {email}')
