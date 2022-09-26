from django.urls import path

from . import views
from . import write_view

app_name = 'blog'

urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<str:slug>', views.post_detail, name="post_detail"),
    path('write', write_view.WriteView.as_view(), name='write'),
    path('<category_name>', views.category, name='category'),
]
