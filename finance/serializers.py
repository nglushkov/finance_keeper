from rest_framework import serializers

from .models import Expense, ExpenseCategory, Currency


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        # fields = ['id', 'amount', 'date', 'description', 'category_id', 'currency_id']
        fields = '__all__'

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Expense` instance, given the validated data.
    #     """
    #     return Expense.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Expense` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance


# class ExpenseCategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ExpenseCategory
#         fields = '__all__'
#
#
# class CurrencySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Currency
#         fields = '__all__'
