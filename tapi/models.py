from django.db import models

# Create your models here.
class Tapi(models.Model):
    TYPEID = models.IntegerField(blank=False, default='',auto_created=False, primary_key=True, serialize=False, verbose_name='TYPEID')
    TYPEDISCRIPTION = models.CharField(max_length=60,blank=False, default='')