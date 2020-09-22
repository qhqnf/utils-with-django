from django.urls import path
from . import views

urlpatterns = [
    path('excel/', views.response_excel),
]