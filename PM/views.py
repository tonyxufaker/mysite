#-*-encoding:utf-8-*-

from django.shortcuts import render
from PM import line_chart


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    city = request.GET.get('city', '')
    if city:
        line_chart.drawLineChart(city)
        img_path = 'PM'+line_chart.drawLineChart(city)
    else:
        img_path = []
    return render(request, 'index.html', {'img_path': img_path})
