from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from business.models import Client
from django.urls import reverse



class Project(models.Model):
    STATUS_CHOICES = (
        ('start','Start'),
        ('discussion', 'Discussion'),
        ('work','Work'),
        ('pause','Pause'),
        ('close','Close'),
        ('finish','Finish'),
    )
    project_name = models.CharField(max_length=250, unique=True, verbose_name='Наименование')
    project_slug = models.SlugField(max_length=250, verbose_name='Slug')
    project_specification_short = models.CharField(max_length=500, blank=True, null=True,
                                                   verbose_name='Короткое описание')
    project_specification_full = models.TextField(blank=True, null=True, verbose_name='Полное описание')
    project_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_projects',
                                        verbose_name='Заказчик')
    project_team_leader = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_projects',
                                            verbose_name='Руководитель разработки')
    project_status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='start', verbose_name='Статус')
    project_date_created = models.DateField(auto_now_add=True, verbose_name='Created')
    project_date_start = models.DateField(verbose_name='Дата начала')
    project_date_finish = models.DateField(verbose_name='Дата завершения')

    class Meta:
        ordering = ('-project_date_start','project_client','project_status',)
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name


    def duration_project(self):
        return (self.project_date_finish-self.project_date_start).days

    def get_absolute_url(self):
        return reverse('project:project', args =[self.project_slug])