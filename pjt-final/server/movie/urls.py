from django.urls import path
from . import views

urlpatterns = [
    path('<movie_id>/detail/', views.detail)
]