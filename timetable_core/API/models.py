from django.db import models
import jsonfield


# Create your models here.

class SchoolModel(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)


class GroupsModel(models.Model):
    json_data = jsonfield.JSONField()
    school_id = models.ManyToManyField(SchoolModel, related_name='school')
    date_create = models


class DisciplinesModel(models.Model):
    json_data = jsonfield.JSONField()
    school_id = models.ManyToManyField(SchoolModel, related_name='school')
    date_create = models


class LoadPlanModel(models.Model):
    json_data = jsonfield.JSONField()
    school_id = models.ManyToManyField(SchoolModel, related_name='school')
    date_create = models


class PedagogsModel(models.Model):
    json_data = jsonfield.JSONField()
    school_id = models.ManyToManyField(SchoolModel, related_name='school')
    date_create = models


class AudiencesModel(models.Model):
    json_data = jsonfield.JSONField()
    school_id = models.ManyToManyField(SchoolModel, related_name='school')
    date_create = models
