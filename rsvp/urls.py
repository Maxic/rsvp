from django.urls import path

from . import views

app_name = 'rsvp'
urlpatterns = [
    path('', views.add_attendee, name='index'),
    #path('test/', views.manage_books, name="test"),
]