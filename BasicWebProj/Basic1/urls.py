from django.conf.urls import url
from . import views

urlpatterns = [
    # /Basic1/
    url(r'^$', views.index, name='index'),

    # /Basic1/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.details, name='details')
]

