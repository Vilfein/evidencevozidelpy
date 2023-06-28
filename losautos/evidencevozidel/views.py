from django.shortcuts import render, redirect

from .forms import DriverForm, CarForm
from .models import Driver, Car

# Create your views here.

def index(req):
    return render(req, 'index.html')


def driver_index(req):
    drivers = Driver.objects.all()
    return render(req, 'driver_index.html', {'drivers': drivers})


def driver_create(req):
    if req.method == 'POST':
        form = DriverForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('driver_index')
    else:
        form = DriverForm()
    return render(req, 'driver_create.html', {'form': form})


def driver_detail(req, pk):
    driver = Driver.objects.filer(pk=pk)
    return render(req, 'driver_detail.html',{'driver': driver})



def car_index(req):
    cars = Car.objects.all()
    return render(req, 'car_index.html', {'cars': cars})


def car_create(req):
    if req.method == 'POST':
        form = CarForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('car_index')
    else:
        form = DriverForm()
    return render(req, 'car_create.html', {'form': form})