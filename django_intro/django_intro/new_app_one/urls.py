from django.urls import path     
from . import views
urlpatterns = [
    path('to_redirect', views.to_redirect),
    path('redirected_route', views.redirected_route)	   
]