from django.conf.urls import urls
from django.contrib import admin

from .views import (
    DogListAPIView
    )

urlpatterns = [
    url(r'^$', DogListAPIView.as_view(), name='list'),
    # url(r'^create/$', dog_create),
    # url(r'^(?P<slug>[\w-])/$', dog_detail, name='detail'),
    # url(r'^(?P<slug>[\w-])/edit/$', dog_update, name='update'),
    # url(r'^(?P<slug>[\w-])/delete/$', dog_delete),
]
