from django.conf.urls import url
from django.contrib import admin

from .views import (
	dog_list,
	dog_create,
	dog_detail,
	dog_update,
	dog_delete,
	)


urlpatterns = [
    url(r'^([0-9]+)/$', views.dog_profile, name="dogprofile"),
    # url(r'^(?P<slug>[\w-]+)/$', dog_detail, name='detail'),
	# url(r'^$', dog_list, name='list'),
    url(r'^new/$', views.dog_post, name="post_dog"),
    # url(r'^create/$', dog_create),
    url(r'^dog_like/$', views.dog_like, name='dog_like'),
    url(r'^delete/(?P<pk>\d+)$', views.dog_delete, name='dog_delete'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', dog_delete),
    url(r'^edit/(?P<pk>\d+)$', views.dog_update, name='dog_update'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', dog_update, name='update'),
]
