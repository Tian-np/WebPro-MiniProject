from django.db import models

# Create your models here.
from django.db.models.deletion import PROTECT
from django.db.models.fields import TimeField


class Faculty(models.Model):
    fac_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # return ให้เห็นเป็นชื่อตอนจะสร้างร้านใหม่อะไรใหม่


class Restaurant(models.Model):
    res_id = models.IntegerField(primary_key=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    picture = models.ImageField()
    open_time = models.TimeField()
    rating = models.FloatField(max_length=255)
    approve_by = models.CharField(max_length=255)
    approve_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


class Food(models.Model):
    food_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    is_vegan = models.BooleanField(default=False)


class RestaurantFood(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    food_id = models.ForeignKey(Food, on_delete=PROTECT)
    price = models.IntegerField()
