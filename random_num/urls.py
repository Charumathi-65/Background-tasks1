from django.urls import path
from .views import run_background_task,get_task_result

urlpatterns = [
    path("run-task/", run_background_task),
    path("result/<str:task_id>/", get_task_result),
]
