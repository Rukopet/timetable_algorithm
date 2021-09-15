from rest_framework import serializers


class GroupSerializer(serializers.Serializer):
    num = serializers.IntegerField(required=True, min_value=0, max_value=20)
    letter = serializers.CharField(required=True, max_length=1, min_length=1)
