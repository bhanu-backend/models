
from django.urls import path
from . import views


urlpatterns = [

  path('',views.app2_home,name = "app2_home"),
]