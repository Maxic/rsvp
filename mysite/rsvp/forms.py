from django.forms import ModelForm
from .models import Attendee
from django.utils.translation import gettext_lazy as _


class Attendeeform(ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'websiteAddress', 'role', 'additionalMessage']

