from rest_framework.response import Response
from rest_framework.views import APIView

from commons.models import IncomeRange, AgeRange, Category
from commons.serializers import RangeSerializer, CategorySerializer


class GetIncomeRanges(APIView):
    def get(self, request):
        incomeRanges = IncomeRange.objects.all()
        RangeSerializer.Meta.model = IncomeRange
        serializer = RangeSerializer(incomeRanges, many=True)
        return Response(serializer.data)


class GetAgeRanges(APIView):
    def get(self, request):
        ageRanges = AgeRange.objects.all()
        RangeSerializer.Meta.model = AgeRange
        serializer = RangeSerializer(ageRanges, many=True)
        return Response(serializer.data)


class GetCategories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
