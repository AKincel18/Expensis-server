from stats.serializers import StatsFilteringSerializer
from stats.services.combined_stats_service import combined_stats
from stats.services.categories_stats_service import categories_stats
from stats.services.separated_stats_service import separated_stats
from stats.stats_class import StatsRequest, StatsName, StatsFilters
from users.service import get_user_by_auth_header


def generate_stats(request_serializer, auth_request):
    user = get_user_by_auth_header(auth_request)
    if user is None:
        return Exception("kaj je user?")  # todo
    filters_serializer = StatsFilteringSerializer(data=request_serializer.data.get('filters'))
    if filters_serializer.is_valid():
        stats_request = StatsRequest(request_serializer.validated_data)
        filters = StatsFilters(filters_serializer.validated_data)

        if stats_request.name == StatsName.CATEGORIES.value:
            return categories_stats(filters, user)
        elif stats_request.name == StatsName.COMBINED.value:
            return combined_stats(filters, user)
        elif stats_request.name == StatsName.SEPARATED.value:
            return separated_stats(filters, user)
