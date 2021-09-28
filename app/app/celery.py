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
    }
}


app.autodiscover_tasks()
