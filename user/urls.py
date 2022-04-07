from django.urls import path
from .views import signupView, loginView, logoutView

app_name = "user"

urlpatterns = [
    path('signup/', signupView.as_view(), name="signup"),
    path('login/', loginView.as_view(), name="login"),
    path('logout/', logoutView.as_view(), name="logout"),
    path('profile/', logoutView.as_view(), name="profile")
]