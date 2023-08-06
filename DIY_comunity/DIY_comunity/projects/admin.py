from django.contrib import admin

from DIY_comunity.projects.models import ProjectModel


# Register your models here.
@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']