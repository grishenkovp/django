from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from project.models import Project
from django.urls import reverse


class Step(models.Model):
    STATUS_CHOICES = (
        ('start','Start'),
        ('discussion', 'Discussion'),
        ('work','Work'),
        ('pause','Pause'),
        ('close','Close'),
        ('finish','Finish'),
    )

    step_project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_steps',
                                        verbose_name='Project')
    step_name = models.CharField(max_length=250, verbose_name='Name')
    step_slug = models.SlugField(max_length=250, verbose_name='Slug')
    step_specification_short = models.CharField(max_length=500, blank=True, null=True,
                                                   verbose_name='Specification_Short')
    step_specification_full = models.TextField(blank=True, null=True, verbose_name='Specification_Full')


    step_status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='start', verbose_name='Status')
    step_date_created = models.DateField(auto_now_add=True, verbose_name='Created')
    step_date_start = models.DateField(verbose_name='Date_start')
    step_date_finish = models.DateField(verbose_name='Date_finish')

    class Meta:
        ordering = ('-step_date_start','step_project','step_status',)
        verbose_name = 'Step'
        verbose_name_plural = 'Steps'

    def __str__(self):
        return self.step_name

    def duration_step(self):
        return (self.step_date_finish - self.step_date_start).days

    def get_absolute_url(self):
        return reverse('step:step', args =[self.id, self.step_slug])