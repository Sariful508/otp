from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('send-otp/', views.send_otp, name='send_otp'),
]