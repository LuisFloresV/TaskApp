from django.views.generic import ListView, DetailView # new 
from django.views.generic.edit import UpdateView, DeleteView, CreateView# new 
from django.urls import reverse_lazy # new
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
import uuid
from allauth.account.views import PasswordChangeView as allauth_PasswordChangeView
from django.urls import reverse_lazy

class TaskCreateNew(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['task']
    
    template_name = 'task_core.html'
    login_url = 'account_login'
    success_url = reverse_lazy('task_core')


    def get_context_data(self, **kwargs):
        return dict(
            super(TaskCreateNew, self).get_context_data(**kwargs),
            tasks=Task.objects.filter(created_by=self.request.user)
        )

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'task_delete.html'
    login_url = 'account_login'
    success_url = reverse_lazy('task_core')

    def dispatch(self, request, *args, **kwargs): # new 
         obj = self.get_object() 
         if obj.created_by != self.request.user: 
             raise PermissionDenied 
         return super().dispatch(request, *args, **kwargs)


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'task_update.html'
    login_url = 'account_login'
    success_url = reverse_lazy('task_core')
    fields = ('task', 'complete')
    def dispatch(self, request, *args, **kwargs): # new 
         obj = self.get_object() 
         if obj.created_by != self.request.user: 
             raise PermissionDenied 
         return super().dispatch(request, *args, **kwargs)




class PasswordChangeView(allauth_PasswordChangeView):
    success_url = reverse_lazy('home')
