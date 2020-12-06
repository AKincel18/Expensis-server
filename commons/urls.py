from django.urls import path

from commons import views

urlpatterns = [
    path('incomeRanges/', views.GetIncomeRanges.as_view()),
    path('ageRanges/', views.GetAgeRanges.as_view()),
    path('categories/', views.GetCategories.as_view())
]
