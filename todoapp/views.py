from django.views.generic import ListView, DetailView # new 
from django.views.generic.edit import UpdateView, DeleteView, CreateView# new 
from django.urls import reverse_lazy # new
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class TaskCreateNew(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title']
    login_url = 'account_login'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    login_url = 'account_login'
    template_name = 'task_list.html'

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)