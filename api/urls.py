from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.APIView.as_view(), name='api_index'),
]