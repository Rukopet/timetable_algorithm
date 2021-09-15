from typing import Type

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import serializers

from .serializers import *
import json

# Create your views here.


class MyUtils:
    @staticmethod
    def json_answer(success: bool, description: str, status: int):
        return HttpResponse(json.dumps({"success": success, "description": description}), status=status,
                            content_type='application/json')


class TimetableBaseView(APIView):
    HTML_FOR_VIEW: str
    SERIALIZER_FOR_VIEW: Type[serializers.Serializer]
    MANY: bool = False

    def get(self, request, slug=None):
        return render(request, self.HTML_FOR_VIEW)

    def post(self, request, slug=None):
        try:
            serializer = self.SERIALIZER_FOR_VIEW(data=request.data, many=self.MANY)
            if serializer.is_valid(raise_exception=True):
                return MyUtils.json_answer(True, "Valid data", 200)
        except ValidationError as e:
            return MyUtils.json_answer(False, f"Bad data, check JSON {e.__str__()}", 422)
        except Exception as e:
            return MyUtils.json_answer(False, f"Unknown error {e.__str__()}", 404)


class GroupsView(TimetableBaseView):
    HTML_FOR_VIEW = 'API/groups.html'
    SERIALIZER_FOR_VIEW = GroupsSerializer


class AudiencesView(TimetableBaseView):
    HTML_FOR_VIEW = 'API/audiences.html'
    SERIALIZER_FOR_VIEW = AudiencesSerializer
    MANY = True


class DisciplinesView(TimetableBaseView):
    HTML_FOR_VIEW = 'API/disciplines.html'
    SERIALIZER_FOR_VIEW = DisciplinesSerializer
    MANY = True


class LoadPlanView(TimetableBaseView):
    HTML_FOR_VIEW = 'API/loadplan.html'
    SERIALIZER_FOR_VIEW = LoadPlanSerializer
    MANY = True


class PedagogsView(TimetableBaseView):
    HTML_FOR_VIEW = 'API/pedagogs.html'
    SERIALIZER_FOR_VIEW = PedagogsSerializer
    MANY = True
