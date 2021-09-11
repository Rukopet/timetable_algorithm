from rest_framework import serializers


class AudiencesParamsSerializer(serializers.Serializer):
    discipline = serializers.CharField(required=False)


class AudiencesListSerializer(serializers.Serializer):
    number_audience = serializers.IntegerField(required=True)
    link_flags = serializers.IntegerField(required=True, min_value=0, max_value=3)
    # params = serializers.ListSerializer(child=AudiencesParamsSerializer())


class AudiencesSerializer(serializers.Serializer):
    audiences = serializers.ListSerializer(required=False, child=AudiencesListSerializer())
