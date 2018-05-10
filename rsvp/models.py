from django.db import models


ROLE_CHOICES = (
    ('Bachelorstudent','Bachelor student'),
    ('Masterstudent', 'Master student'),
    ('Alumnus','Alumnus'),
    ('Other','Other'),
)

TAKEPART_CHOICES = (
    ('Yes','Yes'),
    ('No', 'No'),
)


class Attendee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    websiteAddress = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Alumnus')
    takePart = models.BooleanField(default=False)
    additionalMessage = models.TextField(blank=True)
    artwork1Title = models.CharField(max_length=100, blank=True)
    artwork1SizeH = models.IntegerField(blank=True, null=True)
    artwork1SizeW = models.IntegerField(blank=True, null=True)
    artwork1Price = models.PositiveIntegerField(null=True, blank=True)
    artwork2Title = models.CharField(max_length=100, blank=True)
    artwork2SizeH = models.IntegerField(blank=True, null=True)
    artwork2SizeW = models.IntegerField(blank=True, null=True)
    artwork2Price = models.PositiveIntegerField(null=True, blank=True)
    artwork3Title = models.CharField(max_length=100, blank=True)
    artwork3SizeH = models.IntegerField(blank=True, null=True)
    artwork3SizeW = models.IntegerField(blank=True, null=True)
    artwork3Price = models.PositiveIntegerField(null=True, blank=True)