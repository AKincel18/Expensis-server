from stats.serializers import StatsFilteringSerializer
from stats.services.combined_stat_service import combined_stat
from stats.services.categories_stat_service import categories_stat
from stats.stats_class import StatsRequest, StatsName, StatsFilters
from users.service import get_user_by_auth_header


def generate_stat(request_serializer, auth_request):
    user = get_user_by_auth_header(auth_request)
    if user is None:
        return Exception("kaj je user?")  # todo
    filters_serializer = StatsFilteringSerializer(data=request_serializer.data.get('filters'))
    if filters_serializer.is_valid():
        stats_request = StatsRequest(request_serializer.validated_data)
        filters = StatsFilters(filters_serializer.validated_data)

        if stats_request.name == StatsName.CATEGORIES.value:
            return categories_stat(filters, user)
        elif stats_request.name == StatsName.COMBINED.value:
            return combined_stat(filters, user)
