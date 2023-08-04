from django import forms
from django.forms import fields, widgets
from .models import Post, Comment


class CommentForm(forms.ModelForm):
    body_text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control custom-text', 'cols': '40', 'row': '80'}), label='')

    class Meta:
        model = Comment
        fields = ['body_text', ]
