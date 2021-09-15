from rest_framework import serializers


class DisciplinesPairSerializer(serializers.Serializer):
    discipline = serializers.CharField(required=True)


class DisciplinesSerializer(DisciplinesPairSerializer):
    pair = serializers.ListSerializer(required=False, child=DisciplinesPairSerializer())
