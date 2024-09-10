from django.db import models

from django.utils import timezone

class FoodBank(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

# storage for donor details
class Donor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

# storage for donation details
class FoodDonation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, blank=True, null=True)
    food_item = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField()
    type = models.CharField(max_length=255)
    date_donated = models.DateTimeField(default=timezone.now)
    food_bank = models.ForeignKey(FoodBank,on_delete=models.CASCADE)
    
# storage for tracking food distribution
class Distribution(models.Model):
    food_donation = models.ForeignKey(FoodDonation, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    recipient_location = models.CharField(max_length=255)
    date_distributed = models.DateTimeField(default=timezone.now)
    