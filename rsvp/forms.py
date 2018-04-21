from django.forms import ModelForm
from .models import Attendee


class Attendeeform(ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'websiteAddress', 'role', 'takePart', 'additionalMessage']


