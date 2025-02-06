from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.contrib.auth import login
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required


def hello(request):
    return render(request, 'hello.html')


@login_required
def event_list(request):
    events = Event.objects.filter(user=request.user)  # Načteme pouze události přihlášeného uživatele
    return render(request, 'events/event_list.html', {'events': events})


@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Každá událost patří uživateli
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'events/add_event.html', {'form': form})


@login_required
def edit_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if event.user != request.user:
        return redirect('event_list')  # Zabráníme cizímu uživateli upravit událost

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html', {'form': form, 'event': event})



def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)  # Načteme událost
    if request.method == "POST":
        event.delete()
        return redirect('event_list')  # Přesměrování po smazání

    return render(request, 'events/delete_event.html', {'event': event})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automaticky přihlásíme uživatele
            return redirect('event_list')
    else:
        form = RegisterForm()

    return render(request, 'events/register.html', {'form': form})


def not_logged_in(request):
    return render(request, 'events/not_logged_in.html')

