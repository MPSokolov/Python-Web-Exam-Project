from django.contrib import admin

from DIY_comunity.categories.models import CategoryModel


# Register your models here.
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
