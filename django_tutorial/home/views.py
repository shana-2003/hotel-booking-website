from django.shortcuts import redirect, render
from django.http import  HttpResponse, HttpResponseRedirect
from .models import menu, deals
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def menus(request):
    dict_menu={
        'menu':menu.objects.all()
    }
    return render(request,'menu.html',dict_menu)
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirm.html')
    form = BookingForm()
    dict_form = {
        'form':form
    }
    return render(request,'booking.html', dict_form )
def dealss(request):
    dict_deals={
        'deals':deals.objects.all()
      }
    return render(request,'deal.html',dict_deals)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
