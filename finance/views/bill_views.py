from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.models import Expense, Income, Bill
from finance.serializers import ExpenseSerializer, IncomeSerializer, BillSerializer


class BillList(APIView):
    def get(self, request):
        expenses = Bill.objects.all()
        serializer = BillSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BillDetail(APIView):
    def get_object(self, pk):
        try:
            return Bill.objects.get(pk=pk)
        except Bill.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = BillSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        serializer = BillSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
