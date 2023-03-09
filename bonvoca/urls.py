
from django.contrib import admin
from django.urls import path,include

from vocap import views as vocap_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",vocap_views.index, name='index'),
    path('weather/', vocap_views.weather, name='weather'),

]
