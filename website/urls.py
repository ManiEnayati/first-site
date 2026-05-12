from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
]