from django.shortcuts import render
from .models import Donor, FoodDonation, Distribution

import logging
logger = logging.getLogger(__name__)

#display all donations
def donation_list(request):
    print("Donation list view called")
    donations = FoodDonation.objects.all()
    return render(request, 'donations/donation_list.html', {'donations': donations})

#display all distributions
def distribution_list(request):
    print("Distribution list view called")
    distributions = Distribution.objects.all()
    return render(request, 'donations/distribution_list.html', {'distributions': distributions})