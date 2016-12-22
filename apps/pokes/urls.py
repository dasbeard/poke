from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pokes/(?P<id>\d+)$', views.poke, name='poke'),

]
