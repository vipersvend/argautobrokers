from django.db import models
from datetime import datetime
from brokers.models import Brokers 

class Listing(models.Model):
  Brokers = models.ForeignKey(Brokers, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100) 
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  color = models.CharField(max_length=140, default='Color')
  transmission = models.CharField(max_length=140, null=True)
  Year = models.IntegerField(default=0)
  drivertrain = models.CharField(max_length=30, default='FWD')
  Mileage = models.IntegerField(default=0)
  photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title
