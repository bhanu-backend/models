
from django.contrib import admin
from django.urls import path,include
print(1)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    #path('new/',include('f1.urls')),
]