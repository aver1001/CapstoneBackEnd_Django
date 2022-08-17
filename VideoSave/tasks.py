from celery import shared_task
import time


@shared_task
def sum(x, y):
    return x+y


@shared_task(bind=True)
def debug_task(self):
    print('Hello')


@shared_task
def Check():
    time.sleep(1)
    print('True')
    return True
