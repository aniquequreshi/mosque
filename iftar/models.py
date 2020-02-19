from django.db import models
from django.urls import reverse
import datetime
import uuid

# Create your models here.
class Need (models.Model):
#    id= models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    description = models.CharField(max_length=300)
    display_order = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class Donor (models.Model):
    FOOD_OR_CASH_CHOICE = [
        ('Cash', 'I will give cash.'),
        ('Food', 'I will bring food.'),
    ]
    need = models.OneToOneField(Need, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    food_or_cash = models.CharField(max_length=4, choices = FOOD_OR_CASH_CHOICE) #food or money
    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('iftar:index')
