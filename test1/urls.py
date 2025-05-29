
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
print(1)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
     path('app2/',include('app2.urls')),
    #path('new/',include('f1.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)