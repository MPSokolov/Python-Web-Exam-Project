from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from DIY_comunity.categories.models import CategoryModel

UserModel = get_user_model()


class ProjectModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    materials_used = models.TextField()
    steps = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
