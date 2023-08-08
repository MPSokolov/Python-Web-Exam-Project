from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin, UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model

from DIY_comunity.accounts.models import ProfileModel

UserModel = get_user_model()


def user_can_edit_or_delete(user, profile):
    return user == profile.user


class AnonymousRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redirect to a URL when the user is logged in
        return super().dispatch(request, *args, **kwargs)


class RegisterUserView(AnonymousRequiredMixin, views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        if self.request.POST['next'] != '':
            return self.request.POST['next']
        return reverse_lazy('index')


class LoginUserView(AnonymousRequiredMixin, auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    model = ProfileModel
    template_name = 'accounts/profile-details-page.html'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        user = get_object_or_404(UserModel, username=username)
        return user.profilemodel


class ProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = ProfileModel
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'about_me', 'profile_picture']

    # form_class = ProjectForm

    def get_object(self, queryset=None):
        return self.request.user.profilemodel

    def get_success_url(self):
        return reverse('profile details', kwargs={'username': self.request.user.username})


class ProfileDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user
