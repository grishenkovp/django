from django.db import models

class City(models.Model):

    city_name = models.CharField(max_length=250, verbose_name='Наименование')
    city_country = models.CharField(max_length=250, verbose_name='Страна')

    class Meta:
        ordering = ('city_country',)
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city_name



class Client(models.Model):

    client_name = models.CharField(max_length=250, verbose_name='Наименование')
    client_address = models.ForeignKey(City, models.SET_NULL, blank=True, null=True, related_name='city_clients',
                                       verbose_name='Адрес')

    class Meta:
        ordering = ('client_address',)
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.client_name