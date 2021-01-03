from commons.models import AgeRange
from commons.serializers import RangeSerializer


def get_all_age_ranges():
    age_ranges = AgeRange.objects.all()
    RangeSerializer.Meta.model = AgeRange
    serializer = RangeSerializer(age_ranges, many=True)
    return serializer.data
