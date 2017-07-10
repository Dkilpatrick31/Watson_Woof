# main_app/urls.py
from django.conf.urls import url
from main_app import views
from views import index
from views import dogprofile
from views import post_dog

urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.dogprofile, name="dogprofile"),
    url(r'^new/$', views.post_dog, name="post_dog"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^like_dog/$', views.like_dog, name='like_dog'),
    url(r'^$', views.index, name="index")
]
