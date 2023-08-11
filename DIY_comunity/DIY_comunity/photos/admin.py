from django.contrib import admin

from DIY_comunity.photos.models import PhotoModel


# Register your models here.
@admin.register(PhotoModel)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['creator', 'project', 'image']
    search_fields = ['creator__username', 'project__title']
