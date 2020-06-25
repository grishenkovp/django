from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from step.models import Step
from django.urls import reverse


class Task(models.Model):
    STATUS_CHOICES = (
        ('start','Start'),
        ('discussion', 'Discussion'),
        ('work','Work'),
        ('pause','Pause'),
        ('close','Close'),
        ('finish','Finish'),
    )
    task_step = models.ForeignKey(Step, on_delete=models.CASCADE, related_name='step_tasks',
                                        verbose_name='Step')
    task_name = models.CharField(max_length=250, verbose_name='Name')
    task_slug = models.SlugField(max_length=250, verbose_name='Slug')
    task_specification = models.CharField(max_length=500, blank=True, null=True,
                                                   verbose_name='Specification')
    task_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_tasks',
                                            verbose_name='User')
    task_status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='start', verbose_name='Status')
    task_date_created = models.DateField(auto_now_add=True, verbose_name='Created')
    task_date_start = models.DateField(verbose_name='Date_start')
    task_date_finish = models.DateField(verbose_name='Date_finish')

    class Meta:
        ordering = ('-task_date_start','task_step','task_status',)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task_name


    def duration_task(self):
        return (self.task_date_finish - self.task_date_start).days

    def get_absolute_url(self):
        return reverse('task:task', args =[self.id, self.task_slug])