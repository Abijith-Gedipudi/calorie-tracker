from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class FoodTable(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Calories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(FoodTable, on_delete=models.CASCADE, related_name='consumed_by_users')
