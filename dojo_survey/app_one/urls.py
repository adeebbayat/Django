from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('submit_survey',views.submit_survey),
    path('result',views.result)
]