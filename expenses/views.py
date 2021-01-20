import django.utils.timezone as timezone
from django.core.paginator import Paginator
from django.db.models import Sum
from django.db.models.functions import Coalesce
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from MainExpensis.error_messages import expense_value_cannot_be_negative_error
from expenses.models import Expense
from expenses.serializers import ExpenseSerializerPost, ExpenseSerializerGet
from expenses.service import get_expense_by_id
from stats.services.update_stats_service import update_stats_delete, update_stats_create_update
from stats.stats_class import ExpenseAction
from users.service import get_user_by_auth_header


class ExpenseList(APIView):
    """ Create a new expense """

    def post(self, request):
        serializer = ExpenseSerializerPost(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['value'] < 0:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=expense_value_cannot_be_negative_error)
            serializer.validated_data['user'] = get_user_by_auth_header(request.headers.get('Authorization'))
            save_resp = serializer.save()
            update_stats_create_update(serializer, ExpenseAction.CREATE)
            return Response(ExpenseSerializerGet(save_resp).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """ Get expenses by logged user"""

    def get(self, request):
        user = get_user_by_auth_header(request.headers.get('Authorization'))  # get user by auth header
        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        title_filter = request.GET.get(key='title', default='')
        page_size_filter = request.GET.get(key='pageSize')
        page_index_filter = request.GET.get(key='pageIndex')
        year_filter = request.GET.get(key='year', default=timezone.now().year)
        month_filter = request.GET.get(key='month', default=timezone.now().month)

        expenses = Expense.objects.filter(user=user,
                                          title__icontains=title_filter,
                                          date__year=int(year_filter),
                                          date__month=int(month_filter))
        max_expense_count = expenses.count()

        expenses = expenses.order_by('-date', '-id')

        if page_size_filter is not None and page_index_filter is not None:
            paginator = Paginator(expenses, int(page_size_filter))
            if int(page_index_filter) in paginator.page_range:
                expenses = paginator.page(int(page_index_filter)).object_list
        serializer = ExpenseSerializerGet(expenses, many=True)
        headers = {'X-MAX-RESULTS': max_expense_count}
        return Response(serializer.data, headers=headers)


class ExpenseDetail(APIView):
    """ update expense """

    def put(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        token_user = get_user_by_auth_header(request.headers.get('Authorization'))
        old_value = expense.value
        if expense is None or expense.user != token_user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ExpenseSerializerPost(expense, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = expense.user
            save_resp = serializer.save()
            update_stats_create_update(serializer, ExpenseAction.UPDATE, old_value)
            return Response(ExpenseSerializerGet(save_resp).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """delete expense"""

    def delete(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        if expense is None or expense.user != get_user_by_auth_header(request.headers.get('Authorization')):
            return Response(status=status.HTTP_404_NOT_FOUND)
        expense.delete()
        update_stats_delete(expense)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        if expense is None or expense.user != get_user_by_auth_header(request.headers.get('Authorization')):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializerGet(expense)
        return Response(serializer.data)


class MonthlyExpenseSum(APIView):

    def get(self, request):
        user = get_user_by_auth_header(request.headers.get('Authorization'))  # get user by auth header
        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        year_filter = request.GET.get(key='year', default=timezone.now().year)
        month_filter = request.GET.get(key='month', default=timezone.now().month)

        expenses = Expense.objects.filter(user=user)
        expenses = expenses.filter(date__year=int(year_filter))
        expenses = expenses.filter(date__month=int(month_filter))
        return Response(expenses.aggregate(sum=Coalesce(Sum('value'), 0))['sum'])
