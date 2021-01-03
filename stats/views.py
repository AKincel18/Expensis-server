from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from stats.serializers import StatsFilteringSerializer, StatsRequestSerializer, StatsResponseSerializer
from stats.services.get_stats_service import get_category_stats
from stats.stats_class import StatsFilters, StatsRequest


# path: stats/
class GetStats(APIView):
    """ get stats by request params """

    def get(self, request):
        main_serializer = StatsRequestSerializer(data=request.data)
        if main_serializer.is_valid():
            filters_serializer = StatsFilteringSerializer(data=main_serializer.data.get('filters'))
            if filters_serializer.is_valid():
                stats_request = StatsRequest(main_serializer.validated_data)
                filters = StatsFilters(filters_serializer.validated_data)
                response = get_category_stats(request.headers.get('Authorization'), stats_request, filters)
                serializer = StatsResponseSerializer(response, many=True)
                return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
