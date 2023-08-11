from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from .models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'about_me', 'profile_picture']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last'}),
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'placeholder': '01/01/2000'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0123456789'}),
            'about_me': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'I am me', 'style': 'height: 6rem;'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'profile_picture': ''
        }


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
