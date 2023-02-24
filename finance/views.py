from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from finance.models import Expense
from .serializers import ExpenseSerializer


# class ExpenseList(generics.ListCreateAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer
#
#     def perform_create(self, serializer):
#         expense = serializer.validated_data
#         send_mail(
#             'Subject here',
#             str(expense['amount']),
#             'from@example.com',
#             ['to@example.com'],
#             fail_silently=False,
#         )
#
#
# class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Expense.objects.all()
#     serializer_class = ExpenseSerializer

class ExpenseList(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetail(APIView):
    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @csrf_exempt
# def expense_list(request):
#     """
#     List all code expenses, or create a new expense.
#     """
#     if request.method == 'GET':
#         expenses = Expense.objects.all()
#         serializer = ExpenseSerializer(expenses, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         try:
#             data = JSONParser().parse(request)
#         except ParseError:
#             return HttpResponse(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
#
#         serializer = ExpenseSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def expense_detail(request, pk):
#     try:
#         expense = Expense.objects.get(pk=pk)
#     except Expense.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ExpenseSerializer(expense)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         try:
#             data = JSONParser().parse(request)
#         except ParseError:
#             return HttpResponse(status=422)
#
#         serializer = ExpenseSerializer(expense, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         expense.delete()
#         return HttpResponse(status=204)
