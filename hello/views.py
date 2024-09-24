from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings
from django.http import HttpResponse
import logging
from .forms import BasicForm

def hello_world(request):
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
        # Can set the values here or in the home.html template, if you set them in the home.html template it will override whatever is passed in here
    return render(request, 'home.html', {
        'form': form,
        'action': reverse('home'),  # Set the action to the home URL
        'method': 'post',  # Default method
        'button_text': 'Registerrrrr',
        'button_class': 'btn btn-success',
        'form_class': 'custom-form-class',
    })

def django_components(request):
    return render(request, 'django_components.html')

def view_component(request):
    return render(request, 'view_component.html')
    