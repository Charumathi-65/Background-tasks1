import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.broker_url = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
app.conf.result_backend = app.conf.broker_url