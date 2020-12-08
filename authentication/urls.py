from django.urls import path
from authentication import views

urlpatterns = [
    path('auth/', views.Authentication.as_view()),
    path('refresh/', views.RefreshToken.as_view()),
]
