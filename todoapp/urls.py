from django.urls import path
from .views import *


urlpatterns = [
    path('new/',TaskCreateNew.as_view(), name='task_new'), 
    path('list/',TaskListView.as_view(), name='task_list'), 

    ]