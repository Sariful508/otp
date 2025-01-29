from django import forms

class OTPRequestForm(forms.Form):
    reference_id = forms.CharField(max_length=100)
    mobile_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    send_via = forms.ChoiceField(choices=[('whatsapp', 'WhatsApp'), ('email', 'Email'), ('sms', 'SMS')])