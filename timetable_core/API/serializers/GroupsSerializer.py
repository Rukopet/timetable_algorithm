from rest_framework import serializers


class GroupsListSerializer(serializers.Serializer):
    number = serializers.IntegerField(required=True, min_value=0, max_value=20)
    count = serializers.IntegerField(required=True, min_value=1, max_value=30)
    saturday_not_study = serializers.BooleanField(required=True)
    second_shift_study = serializers.BooleanField(required=True)


class GroupsSerializer(serializers.Serializer):
    second_shift = serializers.BooleanField(required=True)
    max_days = serializers.IntegerField(required=True, min_value=1, max_value=7)
    groups = serializers.ListSerializer(required=True, child=GroupsListSerializer())
