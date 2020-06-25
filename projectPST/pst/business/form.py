from django import forms
from .models import Client, City

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'