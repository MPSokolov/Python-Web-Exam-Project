from django.contrib import admin

from DIY_comunity.accounts.models import ProfileModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'profile_picture']
    list_filter = ['user__is_staff', 'user__is_superuser']
    search_fields = ['user__username', 'first_name', 'last_name', 'email', 'phone_number']
    fieldsets = (('Personal info', {'fields': ('user', 'first_name', 'last_name', 'email')}),
                 ('Advanced options',
                  {'classes': ('collapse',), 'fields': ('date_of_birth', 'phone_number', 'about_me', 'profile_picture',), }),)
