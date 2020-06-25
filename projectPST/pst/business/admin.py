from django.contrib import admin
from .models import City, Client

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name','city_country')
    list_filter = ('city_name','city_country')
    search_fields = ('city_name',)
    ordering = ('city_country','city_name',)


@admin.register(Client)
class CityAdmin(admin.ModelAdmin):
    list_display = ('client_name','client_address')
    list_filter = ('client_name','client_address')
    search_fields = ('client_address',)
    ordering = ('client_address','client_name',)
