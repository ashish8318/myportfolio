from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name="index"),
    path('sendlink/',views.sendlink,name="sendlink"),
    path('receivelink/',views.contectmessage,name="contect")
]
