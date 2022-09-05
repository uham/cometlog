from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    path('signin/', auth_views.LoginView.as_view(template_name='account/signin.html'), name='signin'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]