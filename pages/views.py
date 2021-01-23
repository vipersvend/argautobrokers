from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, Year_choices, state_choices

from listings.models import Listing
from brokers.models import Brokers

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'Year_choices': Year_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all brokers
    brokers = Brokers.objects.order_by('-hire_date')

    # Get MVP
    mvp_brokers = Brokers.objects.all().filter(is_mvp=True)

    context ={
        'brokers': brokers,
        'mvp_brokers': mvp_brokers
    }

    return render(request, 'pages/about.html', context)