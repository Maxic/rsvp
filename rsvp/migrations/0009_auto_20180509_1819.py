# Generated by Django 2.0.4 on 2018-05-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0008_auto_20180509_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='artwork1Price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='artwork2Price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='attendee',
            name='artwork3Price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True),
        ),
    ]
