from django.urls import path
from .views import HomeView,DeleteView,EditView,CompletedView
urlpatterns = [
    path('',HomeView,name='home'),
    path('delete/<int:pk>',DeleteView,name='delete'),
    path('edit/<int:pk>',EditView,name='edit'),
    path('complete/<int:pk>',CompletedView,name='completed'),
]