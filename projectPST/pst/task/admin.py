from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields =        (
                    'task_step',
                    'task_name',
                    'task_slug',
                    'task_specification',
                    'task_user',
                    'task_status',
                    ('task_date_start',
                    'task_date_finish')
                    )
    list_display = (
                    'task_step',
                    'task_name',
                    # 'task_slug',
                    # 'task_specification',
                    'task_user',
                    'task_status',
                    # 'task_date_created',
                    'task_date_start',
                    'task_date_finish'
                    )
    list_editable = ('task_status',)
    list_filter = (
                    'task_step',
                    'task_user',
                   'task_status',
                    )
    search_fields = (
                      'task_specification',
                    )
    prepopulated_fields = {'task_slug':('task_name',)}
    ordering = (
                'task_step',
                'task_user',
                'task_status',
                'task_date_start',
                )