from django.db import models


# Create your models here.
class CreateOperation(models.Model):
    
    operator_type = models.CharField(max_length = 100)
    x = models.IntegerField()
    y = models.IntegerField()

    
    