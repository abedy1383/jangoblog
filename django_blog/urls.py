from django.contrib import admin
from django.urls import path , include
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns





from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('abuot/', views.abuot),
    path('', views.home),
    path('articels' , include('articels.urls'))
]
urlpatterns += staticfiles_urlpatterns()


