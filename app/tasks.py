# Python
# lib
from celery import Celery
# app
from app import config

celery_app = Celery()
celery_app.config_from_object(config)

@celery_app.task()
def add(x, y):
    return x + y

@celery_app.task()
def multiply(x, y):
    return x * y

@celery_app.task()
def negate(x):
    return -x