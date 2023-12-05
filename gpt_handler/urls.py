from django.urls import path

from . import views

app_name = "gpt_handler"

urlpatterns = [
    path('test_API', views.test_API, name='test_API'),
]