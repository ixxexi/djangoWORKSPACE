from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from .models import Auctions, Bids
from django.contrib.auth.models import User

def Index(request):
    # Fetch auctions that are currently active, or use another criterion for "featured"
    featuredAuctions = Auctions.objects.filter(end_time__gt=timezone.now()).order_by('end_time')
    
    # Pass the current time and the featured auctions to the template
    context = {
        'featuredAuctions': featuredAuctions,
        'now': timezone.now(),
    }
    return render(request, 'index.html', context)