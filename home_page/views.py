from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import hotel,Review
from .forms import ReviewFrom


# Create your views here.
def home(request):
    item = hotel.objects.all()
    return render(request, 'home.html', {'item': item})

def search_hotel(request):
    search = request.GET['query']
    s = hotel.objects.filter(area__icontains = search)    
    return render(request, 'search.html', {'details':s})
    

def hotel_detail(request, hotel_id):
    get_hotel = get_object_or_404 (hotel, pk=hotel_id)
    get_review =Review.objects.filter ( Hotel=get_hotel)
    print(get_review)
    return render(request, 'hotel_detail.html', {'details':get_hotel,"review":get_review})


def review(request, hotel_id):
    hotel1 = get_object_or_404(hotel, pk = hotel_id)
    if request.method == "POST":
        form = ReviewFrom(request.POST)
        if form.is_valid():
            reveiw = form.save(commit=False)
            reveiw.Hotel = hotel1
            reveiw.user = request.user
            reveiw.save()
            return redirect('hotel_detail',reveiw.Hotel.id)
    else:
        form = ReviewFrom()
    return render(request,'review_page.html',{'form':form})

def edit_review(request, review_id ):
    review = get_object_or_404(Review, pk = review_id)
    if request.user != review.user:
        return HttpResponse("You are not allowed edit this post")
    if request.method == "POST":
        form = ReviewFrom(request.POST, instance = review )
        if form.is_valid():
            form.save() 
            return redirect('hotel_detail', hotel_id = review.Hotel.id)
    else:
        form = ReviewFrom(instance = review )
    return render(request,'edit.html',{'form':form}) 
def delete(request, review_id):
    review = get_object_or_404(Review, pk = review_id)
    user = request.user
    if review.user.id==user.id:
        review.delete()
        return redirect('hotel_detail',hotel_id=review.Hotel.id)
    else:
        return redirect('hotel_detail', hotel_id = review.Hotel.id)
     



