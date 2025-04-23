from django.urls import path
from .views import training_view
from . import views  # <-- вот это нужно добавить
urlpatterns = [
    path('training/', training_view, name='training'),
]
urlpatterns = [
    path('', views.index, name='index'),
]
