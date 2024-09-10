
from django.urls import path
from . import views


urlpatterns = [
    path(' ', views.donation_list, name='donation_list'),
    path('distributions/', views.distribution_list, name='distribution_list'),
]

