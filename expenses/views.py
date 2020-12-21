from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from MainExpensis.error_messages import access_denied_error
from expenses.models import Expense
from expenses.serializers import ExpenseSerializerPost, ExpenseSerializerGet
from expenses.service import get_expense_by_id
from users.service import get_user_by_id, get_user_by_auth_header


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


class ExpensesByUserId(APIView):
    """get expenses by user id"""

    def get(self, request, user_id):

        user1 = get_user_by_id(user_id)  # get user by id from query param
        user2 = get_user_by_auth_header(request.headers.get('Authorization'))  # get user by auth header
        if user1.id == user2.id:
            expenses = Expense.objects.filter(user=user1)
            serializer = ExpenseSerializerGet(expenses, many=True)
            return Response(serializer.data)
        else:
            return Response(access_denied_error, status=status.HTTP_403_FORBIDDEN)
