from django.shortcuts import render
from .models import *
from faker import Faker
fake = Faker()
import random
from home.thread import CreateStuendtsThread
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
import time
from home import thread

def student_details(request):
    channel_layer = get_channel_layer()
    current_total = 0
    for i in range(self.total):
        current_total += 1
        student_obj = Student.objects.create(
                    student_name = fake.name(),
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10,40)
        )
    return render(request,'index.html')

from django.http import JsonResponse, request
def generate_studen_data(request):
    total = request.GET['total']
    channel_layer = get_channel_layer()
    # data = {"test":"test11"}
    # async_to_sync(channel_layer.group_send)(
    #         'new_consumer_group',{
    #             # type is the function called from consumers
    #             'type':'send_notification',
    #             # this is the value send to send_notification function in consumer
    #             'value': json.dumps(data)
    #         }
    #     )
    # time.sleep(1)
    CreateStuendtsThread(int(total)).start()
    return render(request,'index.html')