from rest_framework import serializers
from . import GroupSerializer


class GroupsForDisciplinesSerializer(serializers.Serializer):
    group = serializers.ListSerializer(required=True, child=GroupSerializer())


class DisciplinesForPedagogs(serializers.Serializer):
    discipline = serializers.CharField(required=True)
    groups = serializers.ListSerializer(required=True, child=GroupsForDisciplinesSerializer())


class PedagogUnitSerializer(serializers.Serializer):
    ped_name = serializers.CharField(required=True)
    disciplines = serializers.ListSerializer(required=True, child=DisciplinesForPedagogs())


class PedagogsSerializer(serializers.Serializer):
    pedagogs = serializers.ListSerializer(required=True, child=PedagogUnitSerializer())
