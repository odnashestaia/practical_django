from django.forms import ModelForm
from .models import Discussion


class DiscussionCreateForms(ModelForm):
    class Meta:
        model = Discussion
        fields = ('title', 'content')
