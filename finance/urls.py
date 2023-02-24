from django.urls import path
from finance import views

urlpatterns = [
    path('expenses/', views.ExpenseList.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetail.as_view()),
]
