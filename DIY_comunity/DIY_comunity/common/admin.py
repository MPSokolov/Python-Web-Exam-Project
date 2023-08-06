from django.contrib import admin

from DIY_comunity.common.models import CommentModel, BookmarkModel, LikeModel


# Register your models here.
@admin.register(LikeModel)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(BookmarkModel)
class BookmarkAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    pass
