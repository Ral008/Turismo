from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from rest_framework import routers
from apps.ciudades.views import CiudadViewSet
from apps.lugares.views import LugarViewSet

router = routers.DefaultRouter()
router.register(r'link-ciudades', CiudadViewSet)
router.register(r'link-lugares', LugarViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Turismo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include(router.urls)),
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),

    #Mostar imagenes
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT, } ),

    #mobil
    url(r'^mobile-ciudades/$', 'apps.ciudades.views.getCiudades', name='getCiudades'),
    url(r'^mobile-lugares/$', 'apps.lugares.views.getLugares', name='getLugares'),
    url(r'^mobile-un-lugar/$', 'apps.lugares.views.getUnLugar', name='getUnLugar'),


)
