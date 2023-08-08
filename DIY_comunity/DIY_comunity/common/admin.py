from django.contrib import admin

from DIY_comunity.common.models import CommentModel, BookmarkModel, LikeModel


# Register your models here.
@admin.register(LikeModel)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'project']


@admin.register(BookmarkModel)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ['user', 'project']


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'content']
