import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from Real_time_data.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Real_time_data.settings')

application = get_asgi_application()




application = get_asgi_application()

# first protocol and then routers
application = get_asgi_application()

ws_patterns = [
    path('ws/student_data/',NewClass),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns)
})