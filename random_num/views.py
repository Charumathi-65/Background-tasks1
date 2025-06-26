from django.http import JsonResponse
from .tasks import generate_random_numbers
from celery.result import AsyncResult
from myproject.celery import app 

def run_background_task(request):
    task=generate_random_numbers.delay()
    return JsonResponse(
        {
        "message": "Task triggered",
        "task_id": task.id
        })

def get_task_result(request, task_id):
    result = AsyncResult(task_id, app=app)
    if result.ready():
        return JsonResponse({
            "status": result.status,
            "result": result.result
        })
    return JsonResponse({
        "status": result.status,
        "result": None
    })