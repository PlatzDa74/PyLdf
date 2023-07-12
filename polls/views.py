from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Poll, Choice

def index(request):
    context = {'umfragen': Poll.objects.all(), 'title': 'Umfragen', 'ueberschrift': 'Umfrage Seite'}
    return render(request, template_name='polls/index.html', context=context)

def umfrage_detail(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage, 'titel': umfrage.name, 'ueberschrift': "Frage"}
    return render(request, template_name='polls/umfrage_detail.html', context=context)

def vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        auswahl = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {'umfrage': umfrage, 'titel': "Abstimmungs Fehler", 'ueberschrift': "Abstimmung gescheitert"}
        return render(request=request, template_name='polls/umfrage_detail.html', context=context)
    else:
        auswahl.votes += 1
        auswahl.save()
        HttpResponseRedirect(reverse('results', args=(umfrage.slug,)))

def results(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage, 'titel': "Ergebnisse", 'ueberschrift': "Ergebnisse"}
    return render(request=request, template_name='polls/results.html', context=context)
