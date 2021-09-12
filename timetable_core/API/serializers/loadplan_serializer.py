from rest_framework import serializers
from .group_serializer import GroupSerializer


class LoadPlanListSerializer(serializers.Serializer):
    discipline = serializers.CharField(required=True)
    load = serializers.IntegerField(required=True, min_value=0)


class LoadPlanSerializer(GroupSerializer):
    discipline = serializers.ListSerializer(required=True, child=LoadPlanListSerializer())
