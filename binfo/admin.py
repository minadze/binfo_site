from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Country, City, Category, Manufacturer, Product, Market, Price, Owner

class MarketInline(admin.StackedInline):
    model = Market
    extra = 1

class CityAdmin(ModelAdmin):
    list_filter = ['country']
    inlines = [MarketInline]

admin.site.register(City, CityAdmin)
admin.site.register(Market)
admin.site.register([Country, Category, Manufacturer, Product, Owner, Price,])

