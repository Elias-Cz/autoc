from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_resp/', views.my_resp, name="my_resp")
]
