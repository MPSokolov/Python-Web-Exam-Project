from django.contrib import admin

from DIY_comunity.common.models import CommentModel, BookmarkModel, LikeModel


# Register your models here.
@admin.register(LikeModel)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'project']
    search_fields = ['user__username', 'project__title']


@admin.register(BookmarkModel)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'project']
    search_fields = ['user__username', 'project__title']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'content']
    search_fields = ['user__username', 'project__title']
