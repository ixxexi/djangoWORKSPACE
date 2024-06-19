from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from .models import Auctions, Bids
from django.contrib.auth.models import User

def Index(request):
    # Fetch auctions that are currently active
    live_Auctions = Auctions.objects.filter(end_time__gt=timezone.now()).order_by('end_time')
    
    # Fetch auctions that have ended
    ended_Auctions = Auctions.objects.filter(end_time__lte=timezone.now()).order_by('-end_time')
    
    # Pass the auctions to the template
    context = {
        'liveAuctions': live_Auctions,
        'endedAuctions': ended_Auctions,
        'now': timezone.now(),
    }
    return render(request, 'index.html', context)
    return render(request, 'index.html', context)