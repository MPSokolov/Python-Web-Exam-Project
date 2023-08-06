from django.contrib.auth import get_user_model
from django.db import models

from DIY_comunity.projects.models import ProjectModel

UserModel = get_user_model()


class BaseModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class LikeModel(BaseModel):

    def __str__(self):
        return f"{self.user.username} liked {self.project.title}"


class BookmarkModel(BaseModel):

    def __str__(self):
        return f"{self.user.username} bookmarked {self.project.title}"


class CommentModel(models.Model):
    content = models.TextField()
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.title}"
