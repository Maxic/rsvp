from django.urls import path

from . import views

app_name = 'rsvp'
urlpatterns = [
    path('', views.add_model, name='index')
]