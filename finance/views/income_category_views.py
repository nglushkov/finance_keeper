from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.models import Income, Income, IncomeCategory
from finance.serializers import IncomeCategorySerializer, IncomeCategorySerializer


class IncomeCategoryList(APIView):
    def get(self, request):
        expenses = IncomeCategory.objects.all()
        serializer = IncomeCategorySerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IncomeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeCategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return IncomeCategory.objects.get(pk=pk)
        except IncomeCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = IncomeCategorySerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        serializer = IncomeCategorySerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
