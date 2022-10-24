from django.urls import path
from main import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('cat/', views.Category.as_view()),
]
