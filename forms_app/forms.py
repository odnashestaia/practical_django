from django import forms
from django.forms import ValidationError
import datetime


class ContactForm(forms.Form):
    date_creation = forms.DateField(initial=datetime.date.today())
    subject = forms.CharField(max_length=100)
    message = forms.CharField(max_length=500)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    # def clean_date_creation(self):
    #     date = self.cleaned_data['date_creation']
    #     if date < datetime.date.today():
    #         raise ValidationError(_("Invalid val"), code='invalid')