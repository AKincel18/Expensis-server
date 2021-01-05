from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from stats.serializers import StatsRequestSerializer, StatsResponseSerializer
from stats.services.generate_stat_service import generate_stat


# path: stats/
class GetStats(APIView):
    """ get stats by request params """

    def get(self, request):
        main_serializer = StatsRequestSerializer(data=request.data)
        if main_serializer.is_valid():
            response = generate_stat(main_serializer, request.headers.get('Authorization'))
            serializer = StatsResponseSerializer(response, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
