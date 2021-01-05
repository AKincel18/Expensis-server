import datetime

from commons.service import get_all_age_ranges


def get_age_range_id_by_user_birth_date(birth_date):
    age = get_user_age(birth_date)
    age_ranges = get_all_age_ranges()
    for age_range in age_ranges:
        if age_range.get("range_from") <= age < age_range.get("range_to"):
            return age_range.get("id")

    # todo exception: not found age range!!!


def get_user_age(birth_date):
    today = datetime.date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def get_value_from_filtering(filtered_value):
    return filtered_value if filtered_value is not None else 0
