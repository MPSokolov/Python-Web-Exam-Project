from django.db import models

from DIY_comunity.projects.models import ProjectModel


class Photo(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_photos/')

    def __str__(self):
        return f"Photo for {self.project.title}"
