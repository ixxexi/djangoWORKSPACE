from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Auctions, Bids
from datetime import timedelta
from decimal import Decimal
from .forms import AuctionForm
from django.contrib.auth.decorators import login_required


def index(request):
    now = timezone.now()
    auctions = Auctions.objects.all()
    liveAuctions = [
        auction
        for auction in auctions
        if auction.start_time + timedelta(seconds=auction.duration) > now
    ]
    endedAuctions = [
        auction
        for auction in auctions
        if auction.start_time + timedelta(seconds=auction.duration) <= now
    ]
    return render(
        request,
        "mainsite/index.html",
        {"liveAuctions": liveAuctions, "endedAuctions": endedAuctions},
    )


@login_required
def auction_detail(request, auction_id):
    auction = get_object_or_404(Auctions, pk=auction_id)
    bids = Bids.objects.filter(auction=auction).order_by("-bid_amount")
    end_time = auction.start_time + timedelta(seconds=auction.duration)
    is_active = end_time > timezone.now()

    highest_bid = bids.first()
    highest_bidder = highest_bid.user.username if highest_bid else None

    if request.method == "POST" and is_active:
        bid_amount = request.POST.get("bid_amount")
        if bid_amount:
            bid_amount = Decimal(bid_amount)
            current_or_starting_bid = (
                auction.current_bid if auction.current_bid else auction.starting_bid
            )
            if bid_amount > current_or_starting_bid:
                new_bid = Bids.objects.create(
                    auction=auction, user=request.user, bid_amount=bid_amount
                )
                auction.current_bid = bid_amount
                auction.save()
                highest_bidder = request.user.username
                messages.success(request, "成功出價！")
                return redirect("auction_detail", auction_id=auction_id)
            else:
                messages.warning(request, "出價金額不得低於目前最高價格。")
        else:
            messages.warning(request, "請輸入有效的出價金額。")

    if is_active:
        endsIn = end_time - timezone.now()
        endsIn = str(endsIn - timedelta(microseconds=endsIn.microseconds))
    else:
        endsIn = "已結束"

    context = {
        "auction": auction,
        "bids": bids,
        "is_active": is_active,
        "endsIn": endsIn,
        "highest_bidder": highest_bidder,
    }
    return render(request, "mainsite/auction_item.html", context)


@login_required
def create_auction(request):
    if request.method == "POST":
        form = AuctionForm(request.POST, request.FILES)
        if form.is_valid():
            auction = form.save(commit=False)
            auction.user = request.user
            auction.save()
            messages.success(request, "刊登成功！")
            return redirect("auction_detail", auction_id=auction.auction_id)
        else:
            messages.warning(request, "請檢查輸入的資料是否正確。")
    else:
        form = AuctionForm()
    return render(request, "mainsite/list_auction.html", {"form": form})
