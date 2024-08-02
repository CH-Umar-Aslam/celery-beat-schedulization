from django.shortcuts import render
# from api.task import test_func
from bgapi.task  import fetch_users
from django.http import HttpResponse
x=1
def test(request):
  test_func.delay()
  return HttpResponse("simple celery worker ")  
def get_users(request):
  ++x
  fetch_users.delay()
  return HttpResponse(f'Current_Status: Total {x*5} seconds and {x} calls')    