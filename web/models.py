from django.db import models
# from web.models import Stu_Class


class Stu_Class(models.Model):
    standard = models.IntegerField()

class StudentDetails(models.Model):
    # id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    guardian_name = models.CharField( max_length=50)
    standard = models.ForeignKey(Stu_Class,related_name='student_class' ,on_delete=models.CASCADE)
    address = models.TextField(max_length=600)
    email = models.EmailField(max_length=254)
    mobile = models.TextField(max_length=10)
    guardian_mobile = models.TextField(max_length=10)

class StudentResult(models.Model):
    roll = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    english = models.IntegerField()
    math = models.IntegerField()
    science = models.IntegerField()
    history = models.IntegerField()
    geography = models.IntegerField()
    total = models.FloatField()
    percent = models.FloatField(null=True)
    grade = models.CharField(null=True,max_length=2)




