from django.conf.urls import url
from testurlapp import views

urlpatterns = [
    url(r'^user/(?<month>\d{2})/(?<year>\d{4})/$', views.home, name='home'),
    #site.com/user/12
    #site.com/usr/12/2000/
]
