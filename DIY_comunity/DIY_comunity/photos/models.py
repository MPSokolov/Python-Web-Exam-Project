from django.contrib.auth import get_user_model
from django.db import models

from DIY_comunity.projects.models import ProjectModel

UserModel = get_user_model()


class PhotoModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_photos/')
    creator = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image}"

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
