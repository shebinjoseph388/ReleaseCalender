from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.CharField(primary_key = True, max_length = 10)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)