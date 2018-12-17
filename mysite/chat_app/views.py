import json

from django.shortcuts import render
from django.utils.safestring import mark_safe


# Create your views here.

def index(request):
    return render(request, 'chat_app/waiting_room.html', {})


def room(request, room_name):
    username = request.user,
    context = {
        'room_name': mark_safe(json.dumps(room_name)),
        'username': username
    }
    return render(request, 'chat_app/chat_.html', context=context)
