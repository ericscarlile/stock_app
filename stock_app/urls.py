from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^searchstocks', views.StockSearchView.as_view(), name='stock_search'),
    url(r'^stock/[A-Z]+', views.StockDetailView.as_view(), name='stock_detail'),
]