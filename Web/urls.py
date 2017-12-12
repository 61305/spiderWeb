from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name='home'),
    url(r'^page/(?P<art_id>[0-9]+)$', views.page, name='page'),
]