from django.urls import path

from . import views

app_name = "webpages"

urlpatterns = [
    path('test_index', views.test_index, name='test_index'),
]