from django.forms import Form
from .models import Driver, Car


class DriverForm(Form):
    class meta:
        model = Driver
        fields = ['name', 'cars']


class CarForm(Form):
    class meta:
        model = Car
        fields = ['brand', 'name', 'driver']

