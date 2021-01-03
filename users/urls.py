from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.SaveUser.as_view()),
]
