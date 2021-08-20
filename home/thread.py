import json
import threading
from .models import *
from faker import Faker
fake = Faker()
import random
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time
import hashlib

class CreateStuendtsThread(threading.Thread):
    
    def __init__(self, total):
        self.total = total
        threading.Thread.__init__(self)

    def run(self):
        try:
            # print('Thread execution started')
            current_total = 0
            for i in range(self.total):
                mystring = str(time.time())
                hash_object = hashlib.md5(mystring.encode())
                SN = hash_object.hexdigest()
                channel_layer = get_channel_layer()

                student_obj = Student.objects.create(
                    student_name = fake.name(),
                    SN = SN,
                    student_email = fake.email(),
                    address = fake.address(),
                    age = random.randint(10,40)
                )
                time.sleep(1)
                current_total += 1
                # channel_layer = get_channel_layer()
                data = {"current_total":current_total,'student_name': student_obj.student_name,'student_email':student_obj.student_email,'student_address':student_obj.address,'student_age':student_obj.age}
                
                # print("=================================================================================")
                # print(data)
                # print("=================================================================================")
                async_to_sync(channel_layer.group_send)(
                'new_consumer_group',{
                    # type is the function called from consumers
                    'type':'send_notification',
                    # this is the value send to send_notification function in consumer
                    'value': json.dumps(data)
                }
            )
                
        except Exception as e:
            print(e)
