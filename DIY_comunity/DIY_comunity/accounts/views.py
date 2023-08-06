from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model


class RegisterUserView(views.CreateView):
    pass


class LoginUserView(auth_views.LoginView):
    pass


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    pass


class ProfileEditView(views.UpdateView):
    pass


class ProfileDeleteView(views.DeleteView):
    pass
