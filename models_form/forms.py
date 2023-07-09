from django import forms
from .models import *
import datetime
from django.utils.translation import gettext_lazy as _


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birthday')
        initial = {
            'birthday': _(datetime.date.today())
        }


# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = '__all__'
#
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
#     birthday = forms.DateField(initial=datetime.date.today(), required=False)


class BookForms(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
