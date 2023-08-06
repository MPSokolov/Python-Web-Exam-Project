from django.contrib import admin

from DIY_comunity.photos.models import PhotoModel


# Register your models here.
@admin.register(PhotoModel)
class PhotoModelAdmin(admin.ModelAdmin):
    pass
