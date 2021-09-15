from rest_framework import serializers

from .int_or_str_field import IntOrString


class AudiencesParamsSerializer(serializers.Serializer):
    num = serializers.IntegerField(required=False, min_value=0, max_value=20)
    letter = serializers.CharField(required=False, max_length=1, min_length=1)
    discipline = serializers.CharField(required=False)


class AudiencesSerializer(serializers.Serializer):
    number_audience = IntOrString(required=True)
    link_flags = serializers.IntegerField(required=True, min_value=0, max_value=3)
    params = serializers.ListSerializer(child=AudiencesParamsSerializer(), allow_null=True)
