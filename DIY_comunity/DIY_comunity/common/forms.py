from django import forms
from .models import CommentModel


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Add comment...',
                })
        }