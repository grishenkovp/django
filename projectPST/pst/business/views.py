from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Client, City
from .form import ClientForm, CityForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

@login_required
def create_client(request):
    new_client = False
    if request.method == 'POST':
        client_form = ClientForm(data=request.POST)
        if client_form.is_valid():
            new_client = client_form.save()
            new_client = True
            return HttpResponseRedirect("/project/")
    else:
        client_form = ClientForm()
    return render(request, 'business/new_client.html', {'new_client': new_client,
                                                                  'form': client_form})

@login_required
def create_city(request):
    new_city = False
    if request.method == 'POST':
        city_form = CityForm(data=request.POST)
        if city_form.is_valid():
            new_city = city_form.save()
            new_city = True
            return HttpResponseRedirect("/project/")
    else:
        city_form = CityForm()
    return render(request, 'business/new_city.html', {'new_city': new_city,
                                                                  'form': city_form})
