from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model


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
    pass


class ProfileEditView(views.UpdateView):
    pass


class ProfileDeleteView(views.DeleteView):
    pass
