from commons.models import AgeRange, IncomeRange
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


def get_all_income_ranges():
    income_ranges = IncomeRange.objects.all()
    RangeSerializer.Meta.model = IncomeRange
    serializer = RangeSerializer(income_ranges, many=True)
    return serializer.data


# return income_range or age_range in a user friendly text
def range_to_string(serializer):
    return str(serializer['range_from']) + ' - ' + str(serializer['range_to'])
