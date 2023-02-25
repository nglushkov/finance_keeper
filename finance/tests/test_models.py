from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from finance.models import ExpenseCategory, Currency, Expense


class ExpenseTestCase(TestCase):
    def setUp(self):
        Currency.objects.create(name="USD", symbol="$")
        ExpenseCategory.objects.create(name="Food")

    def test_expense_category_create(self):
        food = ExpenseCategory.objects.get(name="Food")
        self.assertEqual(food.name, "Food")

    def test_currency_create(self):
        currency = Currency.objects.get(name="USD")
        self.assertEqual(currency.name, "USD")
        self.assertEqual(currency.symbol, "$")

    def test_expense_not_create(self):
        with self.assertRaises(ValidationError):
            Expense.objects.create(
                category_id=ExpenseCategory.objects.get(name="Food"),
                currency_id=Currency.objects.get(name="USD"),
                description="Test expense",
                date=datetime.date(datetime.now()),
                amount='10.0011111111111.11'
            )

    def test_expense_not_create_2(self):
        with self.assertRaises(ValueError):
            Expense.objects.create(
                category_id=100,
                currency_id=Currency.objects.get(name="USD"),
                description="Test expense",
                date=datetime.date(datetime.now()),
                amount='10'
            )

    def test_expense_create(self):
        Expense.objects.create(
            category_id=ExpenseCategory.objects.get(name="Food"),
            currency_id=Currency.objects.get(name="USD"),
            description="Test expense",
            date=datetime.date(datetime.now()),
            amount='120'
        )
        self.assertEqual(Expense.objects.count(), 1)



