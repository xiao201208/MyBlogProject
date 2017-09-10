from . import views
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]