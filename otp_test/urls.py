from django.urls import path
from . import views

urlpatterns = [
    path('send_otp/', views.send_otp, name='send_otp'),
]