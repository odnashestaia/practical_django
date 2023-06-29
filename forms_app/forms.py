from django import forms
from django.forms import ValidationError
from django.utils.translation import gettext as _
import datetime


class ContactForm(forms.Form):
    date_creation = forms.DateField(initial=datetime.date.today(), label='Сегодняшняя дата', label_suffix='23')
    subject = forms.CharField(max_length=100, label='Тема вопроса')
    message = forms.CharField(max_length=500, label='Сообщение')
    sender = forms.EmailField(label='Ваша почта')
    cc_myself = forms.BooleanField(required=False, label='Согласие на отправку')

    def clean_date_creation(self):
        date = self.cleaned_data['date_creation']
        if not date == datetime.date.today():
            raise ValidationError(_('Дата должна быть сегодняшней!'))
        return date