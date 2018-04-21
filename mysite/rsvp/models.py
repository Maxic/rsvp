from django.db import models


ROLE_CHOICES = (
    ('Bachelorstudent','Bachelorstudent'),
    ('Masterstudent', 'Masterstudent'),
    ('Alumnus','Alumnus'),
    ('Other','Other'),
)

class Attendee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    websiteAddress = models.CharField(max_length=200)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Alumnus')
    additionalMessage = models.TextField(blank=True)

