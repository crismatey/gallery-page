from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.detail, name='detail'),
    url(r'^(?P<painting_id>[0-9]+)/$', views.detail, name='detail'),
]
