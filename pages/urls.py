from django.urls import path,include
from .views import *

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about')
    
]