from django import forms

class OTPForm(forms.Form):
    reference_id = forms.CharField(max_length=50, label="Reference ID")
    mobile_number = forms.CharField(max_length=15, label="Mobile Number")
    email = forms.EmailField(label="Email")
    send_via = forms.ChoiceField(
        choices=[('WhatsApp', 'WhatsApp'), ('Email', 'Email'), ('SMS', 'SMS')],
        widget=forms.RadioSelect
    )