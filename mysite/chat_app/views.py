import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


# Create your views here.

def index(request):
    return render(request, 'chat_app/waiting_room.html', {})


def room(request, room_name):
    return render(request, 'chat_app/chat_.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
