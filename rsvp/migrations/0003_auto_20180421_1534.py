# Generated by Django 2.0.4 on 2018-04-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0002_attendee_takepart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='takePart',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=5),
        ),
    ]
