from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    qty = models.IntegerField()
    au_name = models.CharField(max_length=100)

class Fun(models.Model):
    name = models.CharField(max_length=50)