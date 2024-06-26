from django.urls import path
from .auth import login, profile, register, logout

urlpatterns = [
    path('', profile.ProfileView.as_view(), name="profile"),
    path('login/', login.LoginView.as_view(), name="login"),
    path('register/', register.RegisterView.as_view(), name="register"),
    path('logout/', logout.LogoutView.as_view(), name="logout"),
]