from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()



class Add(models.Model):
    name = models.CharField( max_length=50)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    num3 = models.IntegerField()
