from django.urls import path

from stats import views

urlpatterns = [
    path('stats/', views.GetStats.as_view())
]
