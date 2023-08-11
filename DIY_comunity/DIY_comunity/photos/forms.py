from django import forms
from .models import PhotoModel


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ['image']

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'image': "",
        }
