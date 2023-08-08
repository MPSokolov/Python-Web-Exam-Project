from django.contrib import admin

from DIY_comunity.accounts.models import ProfileModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'profile_picture']
    list_filter = ['user__is_staff', 'user__is_superuser']