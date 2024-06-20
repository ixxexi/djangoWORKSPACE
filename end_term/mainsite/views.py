from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone
from .models import Auctions, Bids
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import timedelta
from decimal import Decimal
from .forms import AuctionForm


def index(request):
    now = timezone.now()
    started_auctions = Auctions.objects.filter(start_time__lte=now)
    active_auctions = [auction for auction in started_auctions if auction.start_time + auction.duration >= now]

    return render(request, 'mainsite/index.html', {'active_auctions': active_auctions})

def auction_detail(request, auction_id):
    auction = get_object_or_404(Auctions, pk=auction_id)
    bids = Bids.objects.filter(auction=auction).order_by('-bid_amount')
    end_time = auction.start_time + auction.duration
    is_active = end_time > timezone.now()

    highest_bid = bids.first()
    highest_bidder = highest_bid.user.username if highest_bid else None

    if request.method == "POST" and is_active:
        bid_amount = request.POST.get('bid_amount')
        if bid_amount:
            bid_amount = Decimal(bid_amount)
            current_or_starting_bid = auction.current_bid if auction.current_bid else auction.starting_bid
            if bid_amount > current_or_starting_bid:
                new_bid = Bids.objects.create(auction=auction, user=request.user, bid_amount=bid_amount)
                auction.current_bid = bid_amount
                auction.save()
                highest_bidder = request.user.username
                messages.success(request, "Your bid was placed successfully.")
                return redirect('auction_detail', auction_id=auction_id)
            else:
                messages.error(request, "Your bid must be higher than the current bid.")
        else:
            messages.error(request, "Invalid bid amount.")

    if is_active:
        endsIn = end_time - timezone.now()
        endsIn = str(endsIn - timedelta(microseconds=endsIn.microseconds))
    else:
        endsIn = "Auction has ended"

    context = {
        'auction': auction,
        'bids': bids,
        'is_active': is_active,
        'endsIn': endsIn,
        'highest_bidder': highest_bidder, 
    }
    return render(request, 'mainsite/auction_item.html', context)

def create_auction(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auction_list')  # Adjust the redirect as needed
    else:
        form = AuctionForm()
    return render(request, 'mainsite/list_auction.html', {'form': form})