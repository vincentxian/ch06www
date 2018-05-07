from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request, tvno='0'):
    tv_list = [{'name':'CCTV News', 'tvcode':'yPhFG2I0dE0'},
               {'name':'CCTV Chinese international', 'tvcode':'E1DTZBy4xr4'},]
    
    template = get_template('index.html')
    now = datetime.now()
    tvno = tvno
    tv = tv_list[int(tvno)]
    hour = now.timetuple().tm_hour
    html = template.render(locals())
    return HttpResponse(html)

def carlist(request, maker=0):
    car_maker = ['SAAB', 'Ford', 'Honda', 'Mazda', 'Nissan','Toyota' ]
    car_list = [ [],
                     ['Fiesta', 'Focus', 'Modeo', 'EcoSport', 'Kuga', 'Mustang'],
                                ['Fit', 'Odyssey', 'CR-V', 'City', 'NSX'],
                                ['Mazda3', 'Mazda5', 'Mazda6', 'CX-3', 'CX-5', 'MX-5'],
                                ['Tida', 'March', 'Livina', 'Sentra', 'Teana', 'X-Trail', 'Juke', 'Murano'],
                                ['Camry','Altis','Yaris','86','Prius','Vios', 'RAV4', 'Wish']
                                ]
    maker = int(maker)
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    template = get_template('carlist.html')
    html = template.render(locals())

    return HttpResponse(html)

def carprice(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [[	{'model':'Fiesta', 'price': 203500}, 
                             {'model':'Focus','price': 605000}, 
                                        {'model':'Mustang','price': 900000}],
                    [	{'model':'Fit', 'price': 450000}, 
                                         {'model':'City', 'price': 150000}, 
                                    {'model':'NSX', 'price':1200000}],
                                [	{'model':'Mazda3', 'price': 329999}, 
                                         {'model':'Mazda5', 'price': 603000},
                                        {'model':'Mazda6', 'price':850000}],
                                ]
    maker = int(maker)
    maker_name =  car_maker[maker]
    cars = car_list[maker]
    template = get_template('carprice.html')
    html = template.render(locals())

    return HttpResponse(html)    