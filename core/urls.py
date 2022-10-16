from django.urls import path, include
from .views import IndexView, login, logout, signup

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
]