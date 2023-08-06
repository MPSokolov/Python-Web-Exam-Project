from django import forms
from django.forms import modelformset_factory
from .models import ProjectModel
from DIY_comunity.photos.models import PhotoModel


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        exclude = ['created_at', 'updated_at', 'slug']


