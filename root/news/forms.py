from django.forms import ModelForm
from django import forms
from .models import News

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = "__all__"



