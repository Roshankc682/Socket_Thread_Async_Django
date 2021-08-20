# from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class NewClass(AsyncJsonWebsocketConsumer):
    async def connect(self, *args,**kwargs):
        self.room_name = "new_consumer"
        self.room_group_name = "new_consumer_group"
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connected to new channel '}))

    async def receive(self,text_data):
        # print(text_data)
        await self.send(text_data=json.dumps({'message': 'new channel got message'}))
        # pass

    async def disconnect(self, *args,**kwargs):
        print("disconnected from first")
        # pass

    async def send_notification(self,event):
        print("=================================================================================")
        print(event.get('value'))
        print("=================================================================================")
        date = json.loads(event.get('value'))
        # print(data)
        await self.send(text_data=json.dumps(date))
