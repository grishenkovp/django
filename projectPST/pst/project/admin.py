from django.contrib import admin
from .models import Project
from step.models import Step

class StepInline(admin.TabularInline):
    model = Step
    extra = 0


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields =        (
                    'project_name',
                    'project_slug',
                     ('project_specification_short',
                    'project_specification_full'),
                     ('project_client',
                    'project_team_leader'),
                    'project_status',
                    # 'project_date_created',
                    ('project_date_start',
                    'project_date_finish')
                    )
    list_display = (
                    'project_name',
                    # 'project_slug',
                    # 'project_specification_short',
                    # 'project_specification_full',
                    'project_client',
                    'project_team_leader',
                    'project_status',
                    # 'project_date_created',
                    'project_date_start',
                    'project_date_finish'
                    )
    list_editable = ('project_status',)
    list_filter = (
                    'project_client',
                   'project_team_leader',
                   'project_status'
                    )
    search_fields = (
                      'project_specification_short',
                    )
    prepopulated_fields = {'project_slug':('project_name',)}
    ordering = (
                'project_client',
                'project_status',
                'project_date_start',
                )
    inlines = [
        StepInline,
    ]


