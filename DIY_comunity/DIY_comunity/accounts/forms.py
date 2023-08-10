from django import forms
from .models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'about_me', 'profile_picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
        # labels = {
        #     'location': 'Location',
        #     'date_of_birth': 'Date of Birth',
        #     'first_name': 'First Name',
        #     'last_name': 'Last Name',
        #     'email': 'Email',
        #     'phone_number': 'Phone Number',
        #     'profile_picture': 'Profile Picture',
        # }
