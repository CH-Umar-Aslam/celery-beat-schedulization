from celery import shared_task 
import requests 
from django.http import HttpResponse
@shared_task(bind=True)
def fetch_users(self):
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    data=response.json()
    print(data)
    return "Done"   

