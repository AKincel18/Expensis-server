from rest_framework import serializers
from expenses.models import Expense


class ExpenseSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'date',
            'title',
            'description',
            'category',
            'value'
        ]


class ExpenseSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'user',
            'date',
            'title',
            'description',
            'category',
            'value'
        ]

    category = serializers.SerializerMethodField('get_category_name')

    def get_category_name(self, obj):
        return obj.category.value
