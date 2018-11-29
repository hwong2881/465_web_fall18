from django.urls import path, re_path
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chat_app.consumers import ChatConusmer


application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^(?P<room_name>)/chat", ChatConusmer) #(?P<room_name>)
                    # chat_app.routing.websocket_urlpattern
                ]


            )
        )
    )
})
