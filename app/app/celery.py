import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule ={
    'every-15-seconds': {
        'task': "firstApp.tasks.printing",
        'schedule': 15,
        'args':('pkytsky@gmail.com',)
    },
    'every-30-seconds': {
        'task': "firstApp.tasks.add",
        'schedule': 30,
        'args':(1000,2000)
    }
}


app.autodiscover_tasks()
