
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload_report/', views.afterLogin, name='afterLogin'),
    url(r'^saved/$', views.SaveProfile, name='saved'),
    url(r'^report/$', views.view, name='view'),
    url(r'^logout/$', views.logout, name='logout'),
]