from django.db import models
from django.contrib.postgres.fields import JSONField

class basic_models(models.Model):
    class Meta:
        abstract = True

    def set_data(self, attr, value):
        setattr(self, attr, value)

    def combine_data(self, attr, value):
        if isinstance(self.data, list):
            getattr(self, attr).append(value)
        elif isinstance(self.data, dict):
            getattr(self, attr).update(value)

# Create your models here.
class scheme(basic_models):
    id = models.IntegerField(primary_key=True, db_index=True)
    code = models.CharField(max_length=50)
    data = JSONField()

class user(basic_models):
    id = models.IntegerField(primary_key=True, db_index=True)
    username = models.CharField(max_length=70)
    password = models.CharField(max_length=40)
    rol = models.IntegerField(default=2)
    data = JSONField()