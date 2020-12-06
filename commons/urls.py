from django.urls import path

from commons import views

urlpatterns = [
    path('income-ranges/', views.GetIncomeRanges.as_view()),
    path('age-ranges/', views.GetAgeRanges.as_view()),
    path('categories/', views.GetCategories.as_view())
]
