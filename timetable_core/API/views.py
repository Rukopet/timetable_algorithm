from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import *

import json


# Create your views here.

class MyAnswer:
    @staticmethod
    def json_answer(success: bool, description: str, status: int):
        return HttpResponse(json.dumps({"success": success, "description": description}), status=status,
                            content_type='application/json')


class GroupsView(APIView):
    def get(self, request, slug=None):
        return render(request, 'API/groups.html')

    def post(self, request, slug=None):
        return MyAnswer.json_answer(True, 'yes', 200)


class AudiencesView(APIView):
    def get(self, request, slug=None):
        return render(request, 'API/audiences.html')


class DisciplinesView(APIView):
    def get(self, request, slug=None):
        return render(request, 'API/disciplines.html')

    def post(self):
        ...



class LoadPlanView(APIView):
    def get(self, request, slug=None):
        return render(request, 'API/loadplan.html')


class PedagogsView(APIView):
    def get(self, request, slug=None):
        return render(request, 'API/pedagogs.html')
