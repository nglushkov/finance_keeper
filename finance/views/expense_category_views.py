from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.models import Expense, Income, ExpenseCategory
from finance.serializers import ExpenseCategorySerializer, IncomeSerializer


class ExpenseCategoryList(APIView):
    serializer_class = ExpenseCategorySerializer

    def get(self, request):
        expenses = ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseCategoryDetail(APIView):
    serializer_class = ExpenseCategorySerializer

    def get_object(self, pk):
        try:
            return ExpenseCategory.objects.get(pk=pk)
        except ExpenseCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseCategorySerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseCategorySerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
