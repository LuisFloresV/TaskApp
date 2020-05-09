from django.urls import path  
from .views import *


urlpatterns = [
    path('list/',TaskCreateNew.as_view(), name='task_core'), 
    path('<uuid:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<uuid:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('accounts/password/change/', PasswordChangeView.as_view(), name="account_change_password"),
    ]
    