from django.contrib import admin

from DIY_comunity.accounts.models import ProfileModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    pass