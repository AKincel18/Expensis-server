from rest_framework.response import Response
from rest_framework.views import APIView

from commons.models import IncomeRange, AgeRange, Category
from commons.serializers import RangeSerializer, CategorySerializer


# path: /incomeRanges/
class GetIncomeRanges(APIView):
    """
    get all income ranges
    """
    def get(self, request):
        incomeRanges = IncomeRange.objects.all()
        RangeSerializer.Meta.model = IncomeRange
        serializer = RangeSerializer(incomeRanges, many=True)
        return Response(serializer.data)


# path: /ageRanges/
class GetAgeRanges(APIView):
    """
    get all age ranges
    """
    def get(self, request):
        ageRanges = AgeRange.objects.all()
        RangeSerializer.Meta.model = AgeRange
        serializer = RangeSerializer(ageRanges, many=True)
        return Response(serializer.data)


# path: /categories/
class GetCategories(APIView):
    """
    get all categories
    """
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
