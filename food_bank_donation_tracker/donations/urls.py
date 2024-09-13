
from django.urls import path
from . import views


#urlpatterns = [
#    path(' ', views.donation_list, name='donation_list'),
#    path('add/', views.FoodDonation, name='add_donation'),
#]


urlpatterns = [
    path('', views.home, name='home'),
    ]

