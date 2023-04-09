from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy, reverse
from . import forms

class PhonesListView(ListView):
    model = models.Phones
    template_name = 'project/list.html'
    paginate_by = 4
    def get_queryset(self):
        query_set=super().get_queryset()
        where={}
        q=self.request.GET.get('q',None)
        if q:
            where['title__icontains']=q
        return query_set.filter(**where)


class PhonesCreateView(CreateView):
    model = models.Phones
    form_class = forms.PhonesCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy ('list')

class PhonesUpdateView(UpdateView):
    model = models.Phones
    form_class = forms.PhonesUpdateForm
    template_name = 'project/update.html'
    success_url = reverse_lazy ('list')

class PhonesDeleteView(DeleteView):
    model = models.Phones
    template_name = 'project/delete.html'
    success_url = reverse_lazy ('list')


class TaskCreateView(CreateView):
    model=models.Task
    fields=['description','phones']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('update',args=[self.object.phones.id])

class TaskUpdateView(UpdateView):
    model=models.Task
    fields=['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('update',args=[self.object.phones.id])

class TaskDeleteView(DeleteView):
    model=models.Task

    def get_success_url(self):
        return reverse('update',args=[self.object.phones.id])