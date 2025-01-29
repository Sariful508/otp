from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import OTPRequestForm
from .models import OTPRequest
import random

def send_otp(request):
    if request.method == 'POST':
        form = OTPRequestForm(request.POST)
        if form.is_valid():
            reference_id = form.cleaned_data['reference_id']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            send_via = form.cleaned_data['send_via']

            # Generate a random OTP
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])

            # Save the OTP request to the database
            OTPRequest.objects.create(
                reference_id=reference_id,
                mobile_number=mobile_number,
                email=email,
                otp=otp
            )

            # Send OTP via the selected method (WhatsApp, Email, SMS)
            if send_via == 'whatsapp':
                # Implement WhatsApp OTP sending logic
                pass
            elif send_via == 'email':
                # Implement Email OTP sending logic
                pass
            elif send_via == 'sms':
                # Implement SMS OTP sending logic
                pass

            return JsonResponse({'status': 'success', 'message': 'OTP sent successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'})
    else:
        form = OTPRequestForm()
    return render(request, 'otp_form.html', {'form': form})