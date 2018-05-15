from django.shortcuts import render, redirect, render_to_response
from .forms import Attendeeform
from django.http import HttpResponse
from django.template import loader



def add_attendee(request):
    if request.method == "POST":
        form = Attendeeform(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/rsvp/thanks/?p=%s' % model_instance.id)
    else:
        form = Attendeeform()
        return render(request, "index.html", {'form': form})


def thanks(request):
    data = request.GET
    value = data['p']
    return render(request, "thanks.html", {'data': value})
