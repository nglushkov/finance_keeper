from django.urls import path

from finance.views.bill_views import BillDetail, BillList
from finance.views.currency_views import CurrencyList, CurrencyDetail
from finance.views.exchange_views import ExchangeList, ExchangeDetail
from finance.views.expense_category_views import ExpenseCategoryList, ExpenseCategoryDetail
from finance.views.expense_views import ExpenseList, ExpenseDetail
from finance.views.income_category_views import IncomeCategoryList, IncomeCategoryDetail
from finance.views.income_views import IncomeList, IncomeDetail
from finance.views.movement_views import MovementDetail, MovementList

urlpatterns = [
    path('expenses', ExpenseList.as_view()),
    path('expenses/<int:pk>', ExpenseDetail.as_view()),

    path('incomes', IncomeList.as_view()),
    path('incomes/<int:pk>', IncomeDetail.as_view()),

    path('expense-categories', ExpenseCategoryList.as_view()),
    path('expense-categories/<int:pk>', ExpenseCategoryDetail.as_view()),

    path('income-categories', IncomeCategoryList.as_view()),
    path('income-categories/<int:pk>', IncomeCategoryDetail.as_view()),

    path('currencies', CurrencyList.as_view()),
    path('currencies/<int:pk>', CurrencyDetail.as_view()),

    path('exchange-operations', ExchangeList.as_view()),
    path('exchange-operations/<int:pk>', ExchangeDetail.as_view()),

    path('bills', BillList.as_view()),
    path('bills/<int:pk>', BillDetail.as_view()),

    path('movements', MovementList.as_view()),
    path('movements/<int:pk>', MovementDetail.as_view()),
]
