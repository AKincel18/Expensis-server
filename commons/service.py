from commons.models import AgeRange
from commons.serializers import RangeSerializer


def get_all_age_ranges():
    age_ranges = AgeRange.objects.all()
    RangeSerializer.Meta.model = AgeRange
    serializer = RangeSerializer(age_ranges, many=True)
    return serializer.data


def age_range_to_string(age_range_id):
    age_range = AgeRange.objects.filter(id=age_range_id)
    return str(age_range.get().range_from) + ' - ' + str(age_range.get().range_to)


def full_gender_name(gender):
    return 'Female' if gender == 'F' else 'Male'
