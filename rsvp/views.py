from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.forms.models import inlineformset_factory
from .models import Attendee
from .forms import Attendeeform


def add_attendee(request):
    if request.method == "POST":
        form = Attendeeform(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect('/rsvp')
    else:
        form = Attendeeform()
        return render(request, "index.html", {'form': form})


def add_attendeeOld(request):
    attendee = Attendee()
    artwork = Artwork()
    attendee_form = Attendeeform(instance=attendee) # setup a form for the parent
    artwork_form = Artworkform(instance=artwork) # setup a form for the parent


    #BookInlineFormSet = inlineformset_factory(Attendee, Artwork, fields=('title', 'size', 'price'))
    #formset = BookInlineFormSet(instance=attendee)

    if request.method == "POST":
        attendee_form = Attendeeform(request.POST)

        if id:
            attendee_form = Attendeeform(request.POST, instance=attendee)

        #formset = BookInlineFormSet(request.POST, request.FILES)

        if attendee_form.is_valid():
            created_attendee = attendee_form.save(commit=False)
            created_attendee.save()

            #formset = BookInlineFormSet(request.POST, request.FILES, instance=created_attendee)

            if artwork_form.is_valid():
                artwork_form.save()
                return HttpResponseRedirect(created_attendee.get_absolute_url())

    return render_to_response("index.html", {
        "form": attendee_form,
        "formset": artwork_form,
    })