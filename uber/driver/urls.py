from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^home/$', views.home, name= 'home'),
    url(r'^home2/$', views.home2, name= 'home2'),
    url(r'^d-profile/$', views.d_profile, name='d-profile'),
    url(r'^p-profile/$', views.p_profile, name='p-profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)