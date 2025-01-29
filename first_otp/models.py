from django.db import models

# Create your models here.


class OTPLog(models.Model):
    reference_id = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    send_via = models.CharField(max_length=10, choices=[('WhatsApp', 'WhatsApp'), ('Email', 'Email'), ('SMS', 'SMS')])
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OTP to {self.mobile_number} via {self.send_via}"

