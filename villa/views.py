from django.shortcuts import render
from .models import Properties

# Create your views here.


def index(request):
    
    prop1  = Properties()
    prop1.category = 'Luxuryvilla'
    prop1.price = 2000
    prop1.address = '18 New Street Miami, OR 97219'
    prop1.img = 'property-01.jpg'
    
    prop2  = Properties()
    prop2.category = 'Penthhouse'
    prop2.price = 8000
    prop2.address = '12 New Street Miami, OR 12650'
    prop2.img = 'property-02.jpg'
    
    prop3  = Properties()
    prop3.category = 'Luxuryvilla'
    prop3.price = 4000
    prop3.address = '54 Mid Street Florida, OR 27001'
    prop3.img = 'property-03.jpg'
    
    props = [prop1, prop2, prop3]
    
    return render(request, 'villa/index.html',{'props' : props})