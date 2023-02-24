from rest_framework import serializers

from .models import Expense, ExpenseCategory, Currency, Income, Exchange, Movement, Bill


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'


class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'
