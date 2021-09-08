from django.urls import path
from .views import *


urlpatterns = [
    path('groups/', GroupsView.as_view()),
    path('audiences/', AudiencesView.as_view()),
    path('disciplines/', DisciplinesView.as_view()),
    path('loadplan/', LoadPlanView.as_view()),
    path('pedagogs/', PedagogsView.as_view()),
]
