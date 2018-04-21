from django.forms import ModelForm
from .models import Attendee
from django.utils.translation import ugettext_lazy as _


class Attendeeform(ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'websiteAddress', 'role', 'takePart', 'additionalMessage']
        labels = {
            'takePart': _('Do you want to take part in a physical drawing estafette on the day of the opening?'),
        }


