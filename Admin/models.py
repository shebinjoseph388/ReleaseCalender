from django.db import models

# Create your models here.
class ReleaseTypes(models.Model):
    id = models.AutoField(primary_key = True, max_length = 10)
    release_name = models.CharField(max_length = 50)

class Releases(models.Model):
    id = models.CharField(primary_key = True, max_length = 10)
    name = models.CharField(max_length = 50)
    release_type = models.ForeignKey(ReleaseTypes)
    start_date = models.CharField(max_length = 50)
    end_date = models.CharField(max_length = 50)

