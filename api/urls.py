from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api', views.APIView.as_view(), name='index'),
]