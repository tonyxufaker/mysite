#-*-encoding:utf-8-*-

from django.shortcuts import render
from PM import line_chart

# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    city = request.GET('city')
    src = line_chart.drawLineChart(city)
    return render(request, 'index.html', {'src' : src} )
