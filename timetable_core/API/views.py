from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class GroupsView(View):
    def get(self, request, slug=None):
        return render(request, 'API/groups.html')


class AudiencesView(View):
    def get(self, request, slug=None):
        return render(request, 'API/audiences.html')


class DisciplinesView(View):
    def get(self, request, slug=None):
        return render(request, 'API/disciplines.html')

    def post(self):

        ...


class LoadPlanView(View):
    def get(self, request, slug=None):
        return render(request, 'API/loadplan.html')


class PedagogsView(View):
    def get(self, request, slug=None):
        return render(request, 'API/pedagogs.html')