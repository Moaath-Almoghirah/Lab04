from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tax_rate = 15
def index(request):
    return HttpResponse("<h1>this is a site to calculate tax</h1>")

def anyNumber(request, number):
    if int(number) > 0:
        return HttpResponse(f"<h2>the totals is {int(number)*tax_rate/100+int(number)}</h2>")
    else:
        return HttpResponse("<h1>please enter a valid numerical value </h1>")

def taxrate(request):
    return HttpResponse(f"<h1>The tax rate is {tax_rate}%</h1>")