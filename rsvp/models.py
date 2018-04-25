from django.db import models


ROLE_CHOICES = (
    ('Bachelorstudent','Bachelorstudent'),
    ('Masterstudent', 'Masterstudent'),
    ('Alumnus','Alumnus'),
    ('Other','Other'),
)

TAKEPART_CHOICES = (
    ('Yes','Yes'),
    ('No', 'No'),
)

SIZE_CHOICES = (
    ('A4','A4'),
    ('A3','A3'),
    ('A2','A2'),
    ('A1','A1'),
    ('A0','A0'),
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
    artwork1Price = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True)
    artwork2Title = models.CharField(max_length=100, blank=True)
    artwork2SizeH = models.IntegerField(blank=True, null=True)
    artwork2SizeW = models.IntegerField(blank=True, null=True)
    artwork2Price = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True)
    artwork3Title = models.CharField(max_length=100, blank=True)
    artwork3SizeH = models.IntegerField(blank=True, null=True)
    artwork3SizeW = models.IntegerField(blank=True, null=True)
    artwork3Price = models.DecimalField(decimal_places=2, max_digits=6, default=0, blank=True)



#class Artwork(models.Model):
#    title = models.CharField(max_length=100)
#    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default='A4')
#    price = models.IntegerField()
#    Attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
