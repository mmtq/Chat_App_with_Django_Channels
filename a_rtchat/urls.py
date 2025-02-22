from django.urls import path
from a_rtchat.views import *
app_name = "a_rtchat"  # This defines the namespace
urlpatterns = [
    path('', chat_view, name="chat"),
]