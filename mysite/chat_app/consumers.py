from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        me =self.scope['user']
        print(me, " connected to websocket in room:", room_name)
        # self.room_group_name = "chat_%s" % room_name
        self.accept()



    def disconnect(self, close_code):
        pass


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
