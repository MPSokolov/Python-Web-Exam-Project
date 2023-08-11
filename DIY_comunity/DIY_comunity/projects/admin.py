from django.contrib import admin

from DIY_comunity.projects.models import ProjectModel


# Register your models here.
@admin.register(ProjectModel)
class ProjectModelAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['title', 'description', 'created_at', 'updated_at', 'creator', 'category', 'project_pictures']
    search_fields = ['title', 'description', 'creator__username']
    list_filter = ['category', 'creator']
    fields = ['title', 'description', 'materials_used', 'steps', ('creator', 'category'), 'slug']

    @staticmethod
    def project_pictures(obj):
        return ', '.join(str(pic) for pic in obj.photomodel_set.all())