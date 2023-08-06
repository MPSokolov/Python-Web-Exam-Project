from django.contrib import admin

from DIY_comunity.projects.models import ProjectModel


# Register your models here.
@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    # list_display = ['get_project_pictures']

    # @staticmethod
    # def get_project_pictures(obj):
    #     return ', '.join(str(pic) for pic in obj.photomodel_set.all())