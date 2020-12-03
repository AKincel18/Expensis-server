from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.SaveUser.as_view()),
    path('users/<int:user_id>/', views.UserDetail.as_view()),
]
