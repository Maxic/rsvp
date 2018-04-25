from django.forms import ModelForm
from .models import Attendee
from django import forms


class Attendeeform(ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', 'email', 'websiteAddress', 'role', 'takePart', 'additionalMessage',
                  'artwork1Title', 'artwork1SizeH', 'artwork1SizeW', 'artwork1Price',
                  'artwork2Title', 'artwork2SizeH', 'artwork2SizeW', 'artwork2Price',
                  'artwork3Title', 'artwork3SizeH', 'artwork3SizeW', 'artwork3Price'
                  ]
        widgets = { 'artwork1SizeH': forms.TextInput(attrs={'size': 8}),
                    'artwork1SizeW': forms.TextInput(attrs={'size': 8}),
                    'artwork2SizeH': forms.TextInput(attrs={'size': 8}),
                    'artwork2SizeW': forms.TextInput(attrs={'size': 8}),
                    'artwork3SizeH': forms.TextInput(attrs={'size': 8}),
                    'artwork3SizeW': forms.TextInput(attrs={'size': 8}),
                    }