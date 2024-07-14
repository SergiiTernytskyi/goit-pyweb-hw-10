from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import SigninForm

app_name = "users"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path(
        "signin/",
        LoginView.as_view(
            template_name="users/signin.html",
            form_class=SigninForm,
            redirect_authenticated_user=True,
        ),
        name="signin",
    ),
    path(
        "signout/",
        LogoutView.as_view(template_name="users/signout.html"),
        name="signout",
    ),
]
