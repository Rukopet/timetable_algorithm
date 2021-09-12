from rest_framework import serializers
from . import GroupSerializer


class PedagogsDisciplinesSerializer(serializers.Serializer):
    discipline = serializers.CharField(required=True)
    groups = GroupSerializer(required=True, many=True)


class PedagogsSerializer(serializers.Serializer):
    ped_name = serializers.CharField(required=True)
    disciplines = serializers.ListSerializer(required=True, child=PedagogsDisciplinesSerializer())
