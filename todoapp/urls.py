from django.urls import path
from .views import *


urlpatterns = [
    path('list/',TaskCreateNew.as_view(), name='task_core'), 
    path('<uuid:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<uuid:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    ]
    