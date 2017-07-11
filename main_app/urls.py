from django.conf.urls import url, include
from main_app import views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
# from views import index
# from views import dogprofile
# from views import post_dog
# from views import update_dog

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^([0-9]+)/$', views.dogprofile, name="dogprofile"),
    url(r'^new/$', views.post_dog, name="post_dog"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^like_dog/$', views.like_dog, name='like_dog'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_dog, name='delete_dog'),
    url(r'^edit/(?P<pk>\d+)$', views.update_dog, name='update_dog'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^about/$', views.about, name='about'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    Surl(r'^$', views.index, name="index")
]
