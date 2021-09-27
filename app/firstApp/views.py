from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import tasks
from celery.result import AsyncResult


# Create your views here.

# def home(request):
#     return render(request, "home.html")


def run_task(request):
    # task = tasks.create_task.delay(int(1))
    task = tasks.add.delay(1,2)
    return JsonResponse({"task_id": task.id}, status=202)

def run_task_1sec(request):
    task = tasks.my_task.delay('my_task')
    return JsonResponse({"task_id": task.id}, status=202)

def get_status(request, task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JsonResponse(result, status=200)