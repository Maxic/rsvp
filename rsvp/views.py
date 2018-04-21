from django.shortcuts import render, redirect
from django.views import generic
from .models import Attendee
from .forms import Attendeeform


def add_model(request):
    if request.method == "POST":
        form = Attendeeform(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/rsvp')

    else:

        form = Attendeeform()
        return render(request, "index.html", {'form': form})

