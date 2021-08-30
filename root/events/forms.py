#from django.forms import ModelForm
from django.forms import ModelForm
from django.forms.widgets import Textarea
from .models import Event

class EventForm(ModelForm):
    class Meta(ModelForm):
        model = Event
        fields = "__all__"

"""class EventForm(forms.Form):
    event_name = forms.CharField(label = "event name", max_length = 50)
    event_date = forms.DateField()
    event_start_time = forms.TimeField()
    event_end_time = forms.TimeField()
    description = forms.CharField(widget= Textarea)"""

