# Create your models here.
from django.db import models


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'finance_expense_category'


class IncomeCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'finance_income_category'


class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=10)

    class Meta:
        db_table = 'finance_currency'


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    category_id = models.ForeignKey(ExpenseCategory, on_delete=models.RESTRICT)
    currency_id = models.ForeignKey(Currency, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'finance_expense'
        ordering = ['id']


class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    category_id = models.ForeignKey(IncomeCategory, on_delete=models.RESTRICT)
    currency_id = models.ForeignKey(Currency, on_delete=models.RESTRICT)

    class Meta:
        db_table = 'finance_income'


class ExchangeOperation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    source_currency = models.ForeignKey(Currency, related_name='exchange_sources', on_delete=models.RESTRICT)
    target_currency = models.ForeignKey(Currency, related_name='exchange_targets', on_delete=models.RESTRICT)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'finance_exchange_operation'
