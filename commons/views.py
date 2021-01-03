from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from commons.models import IncomeRange, Category
from commons.serializers import RangeSerializer, CategorySerializer
from commons.service import get_all_age_ranges


# path: /income-ranges/
class GetIncomeRanges(APIView):
    """
    get all income ranges
    """
    permission_classes = [AllowAny]

    def get(self, request):
        income_ranges = IncomeRange.objects.all()
        RangeSerializer.Meta.model = IncomeRange
        serializer = RangeSerializer(income_ranges, many=True)
        return Response(serializer.data)


# path: /age-ranges/
class GetAgeRanges(APIView):
    """
    get all age ranges
    """
    def get(self, request):
        return Response(get_all_age_ranges())


# path: /categories/
class GetCategories(APIView):
    """
    get all categories
    """
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
