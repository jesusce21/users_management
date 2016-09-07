from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class scheme(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    code = models.CharField(max_length=50)
    data = JSONField()

class user(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=40)
    rol = models.IntegerField(default=2)
    data = JSONField()