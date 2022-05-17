from django.db import models

# Create your models here.

class familia2(models.Model):
    name= models.CharField(max_length=40)
    last_name= models.CharField(max_length=40)
    profession= models.CharField(max_length=40)
    age= models.IntegerField()
    birthday=  models.DateField()
