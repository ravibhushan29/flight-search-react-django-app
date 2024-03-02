from django.urls import path
from user_auth.views import LoginViewView, UserSignUpView

urlpatterns = [
    path("signup/", UserSignUpView.as_view(), name="user-signup"),
    path("login/", LoginViewView.as_view(), name="user-login"),
]
