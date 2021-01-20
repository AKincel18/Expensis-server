from django.urls import path

from expenses import views

urlpatterns = [
    path('expenses/', views.ExpenseList.as_view()),
    path('expenses/<int:expense_id>/', views.ExpenseDetail.as_view()),
    path('expenses-sum/', views.MonthlyExpenseSum.as_view())
]
