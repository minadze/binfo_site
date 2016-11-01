from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^countries/$', views.country_list, name='country_list'),
    url(r'^markets/$', views.market_list, name='market_list'),
    url(r'^$', views.index, name='index'),
]
