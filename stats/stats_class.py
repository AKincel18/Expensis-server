from enum import Enum


class StatsResponse:
    def __init__(self, name_value, user_value, all_value):
        self.name_value = name_value
        self.user_value = user_value
        self.all_value = all_value


class StatsRequest:
    def __init__(self, data):
        self.name = data['name']


class StatsFilters:
    def __init__(self, data):
        self.income_range = data['income_range']
        self.age_range = data['age_range']
        self.gender = data['gender']


class ExpenseAction(Enum):
    CREATE = 1,
    UPDATE = 2,
    DELETE = 3


class StatsName(Enum):

    def __str__(self):
        return str(self.value)

    CATEGORIES = "Categories"
    COMBINED = "Combined"
