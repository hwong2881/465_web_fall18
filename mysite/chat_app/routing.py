from channels.routing import route
from chat_app.consumers import ws_connect, ws_disconnect


channel_routing = [
    route("http.request", "chat_app.consumers.http_consumer"),
    route('websocket.connect', ws_connect, path=r'^/chat/$'),
    route('websocket.disconnect', ws_disconnect),
]
# channel_routing
