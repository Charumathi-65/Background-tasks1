from celery import shared_task
import random

@shared_task
def generate_random_numbers(count=10):
    numbers = [random.randint(1, 100) for _ in range(count)]
    print("Generated numbers:", numbers)
    return numbers
