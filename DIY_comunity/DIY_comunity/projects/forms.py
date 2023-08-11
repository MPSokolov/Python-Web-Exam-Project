from django import forms
from django.forms import modelformset_factory
from .models import ProjectModel
from DIY_comunity.photos.models import PhotoModel


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectModel
        exclude = ['created_at', 'updated_at', 'slug', 'creator']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'description', 'style': 'height: 7rem;'}),
            'materials_used': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'materials', 'style': 'height: 9rem;'}),
            'steps': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'steps', 'style': 'height: 13rem;'}),
            'category': forms.Select(attrs={'class': 'form-select', }),
        }

    label_suffix = ''
