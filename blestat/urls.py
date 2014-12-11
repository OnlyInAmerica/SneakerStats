from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views

# Django Rest Framework
router = routers.DefaultRouter()
router.register(r'sessions', views.SessionViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blestat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Django Rest Framework
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


)
