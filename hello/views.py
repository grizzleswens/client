from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings
from django.http import HttpResponse
import logging
from .forms import BasicForm

def hello_world(request):
    radio_options = [
        {'value': 'male', 'label': 'Male', 'checked': True},
        {'value': 'female', 'label': 'Female'},
        {'value': 'other', 'label': 'Other'}
    ]

    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            # Process the form data, e.g., save it to the database
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(name, username, password)
            return redirect('home')
    else:
        form = BasicForm()

    # Combine form context and radio options into one dictionary
    context = {
        'form': form,
        'action': reverse('home'),  # Set the action to the home URL
        'method': 'post',  # Default method
        'button_text': 'Registerrrrr',
        'button_class': 'btn btn-success',
        'form_class': 'custom-form-class',
        'radio_options': radio_options
    }

    return render(request, 'home.html', context)

def django_components(request):
    
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(name, username, password)
            # Process the data (e.g., save to the database)
            return redirect('home')
    else:
        form = BasicForm()

    return render(request, 'django_components.html', {'form': form})

def view_component(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(name, username, password)
            # Process the data (e.g., save to the database)
            return redirect('home')
    else:
        form = BasicForm()

    return render(request, 'view_component.html', {'form': form})
    