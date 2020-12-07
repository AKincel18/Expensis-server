from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from expenses.models import Expense
from expenses.serializers import ExpenseSerializerPost, ExpenseSerializerGet
from expenses.service import get_expense_by_id


class ExpenseList(APIView):
    """ Create a new expense """
    def post(self, request):
        serializer = ExpenseSerializerPost(data=request.data)
        if serializer.is_valid():
            save_resp = serializer.save()
            return Response(ExpenseSerializerGet(save_resp).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """ Get all expenses """
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializerGet(expenses, many=True)
        return Response(serializer.data)


class ExpenseDetail(APIView):
    """ update expense """
    def put(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        if expense is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializerPost(expense, data=request.data)
        if serializer.is_valid():
            save_resp = serializer.save()
            return Response(ExpenseSerializerGet(save_resp).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """delete expense"""
    def delete(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        if expense is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)