from rest_framework import serializers


class StatsFilteringSerializer(serializers.Serializer):
    income_range = serializers.BooleanField()
    age_range = serializers.BooleanField()
    gender = serializers.BooleanField()

    def update(self, instance, validated_data):
        instance.income_range = validated_data.get('income_range', instance.income_range)
        instance.age_range = validated_data.get('age_range', instance.age_range)
        instance.gender = validated_data.get('gender', instance.gender)

    def create(self, validated_data):
        return StatsFilteringSerializer(**validated_data)


class StatsRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    filters = StatsFilteringSerializer()

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.filters = validated_data.get('filters', instance.filters)

    def create(self, validated_data):
        return StatsRequestSerializer(**validated_data)


class StatsResponseSerializer(serializers.Serializer):
    name_value = serializers.CharField()
    user_value = serializers.FloatField()
    all_value = serializers.FloatField()

    def update(self, instance, validated_data):
        instance.name_value = validated_data.get('name_value', instance.name_value)
        instance.user_value = validated_data.get('user_value', instance.user_value)
        instance.all_value = validated_data.get('all_value', instance.all_value)

    def create(self, validated_data):
        return StatsResponseSerializer(**validated_data)
