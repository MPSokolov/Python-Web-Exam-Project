from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from DIY_comunity.categories.models import CategoryModel

UserModel = get_user_model()


class ProjectModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    materials_used = models.TextField()
    steps = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100, blank=True, editable=False)

    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
