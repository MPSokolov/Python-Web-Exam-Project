from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

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


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "class": 'form-control', 'placeholder': 'password'}),
    )


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'username', 'aria-describedby': "usernameHelp"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].widget.attrs['aria-describedby'] = 'pass1Help'
        self.fields['password2'].widget.attrs['aria-describedby'] = 'pass2Help'
