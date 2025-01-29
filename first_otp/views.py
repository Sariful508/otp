
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import OTPForm
from .models import OTPLog
import random


def home(request):
    return HttpResponse("<h1>Welcome to the OTP App</h1>")

def send_otp(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            # Simulate OTP generation and sending
            otp = random.randint(1000, 9999)
            send_via = form.cleaned_data['send_via']
            # Save log (optional)
            OTPLog.objects.create(
                reference_id=form.cleaned_data['reference_id'],
                mobile_number=form.cleaned_data['mobile_number'],
                email=form.cleaned_data['email'],
                send_via=send_via
            )
            # Here you would integrate with an actual service (e.g., Twilio, WhatsApp API, etc.)
            print(f"Sending OTP {otp} via {send_via}")  
            return JsonResponse({'success': True, 'message': f"OTP sent via {send_via}!"})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})




