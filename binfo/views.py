from django.http import HttpResponse
from django.shortcuts import render,render_to_response

# Create your views here.
from django.template import loader
from binfo.models import Country, Market


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def country_list(request):
    context = {'countries': Country.objects.all()}
    template = loader.get_template('country.html')
    return HttpResponse(template.render(context))


def market_list(request):
    context = {'markets': Market.objects.all()}
    template = loader.get_template('markets.html')
    return HttpResponse(template.render(context))
