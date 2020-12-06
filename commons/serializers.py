from rest_framework import serializers

from commons.models import Category


class RangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = None
        fields = [
            'id',
            'range_from',
            'range_to'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'value'
        ]
