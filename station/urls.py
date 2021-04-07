from django.urls import path
from . import views


urlpatterns = [
    path(r'',views.index, name='Welcome'),
    path(r'api/pull', views.pull, name='pull'),
    path(r'api/push',views.push,name='push'),   
]