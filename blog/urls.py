from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.main, name='main'),
    path('<category_name>', views.category, name='category'),
]
