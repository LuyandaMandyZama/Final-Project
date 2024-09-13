#from django.shortcuts import render
#from .models import Donor, FoodDonation, Distribution

#import logging
#logger = logging.getLogger(__name__)

from django.http import HttpResponse
def home(request):
    return HttpResponse("This is the homepage.")