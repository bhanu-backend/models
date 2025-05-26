
from django.urls import path
from . import views
urlpatterns = [

 
    path('f1/',views.home),
    path('s1/',views.set_cokkies),

]
