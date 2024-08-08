from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    )
from .models import Task, Standard, Guestalk
from .consts import ITEM_PER_PAGE

class ListTaskView(LoginRequiredMixin, ListView):
    template_name = 'regular/task_list.html'
    model = Task

class StandardTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_standard.html'
    model = Standard
    fields = ['comment', 'template', 'zoom']

class GuestalkTaskView(LoginRequiredMixin, ListView):
    template_name = 'regular/task_guest_list.html'
    model = Guestalk
    paginate_by = ITEM_PER_PAGE

class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_guest_create.html'
    model = Guestalk
    fields = ['day', 'vol', 'guest', 'guest_url', 'theme', 'comment', 'template', 'thumbnail', 'spreadsheet', 'zoom']
    success_url = reverse_lazy('guestalk-task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    template_name = 'regular/task_guest_update.html'
    model = Guestalk
    fields = ['day', 'vol', 'guest', 'guest_url', 'theme', 'comment', 'template', 'thumbnail', 'spreadsheet', 'zoom']
    success_url = reverse_lazy('guestalk-task')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
def index_view(request):
    object_list = Task.objects.order_by('-id')

    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'regular/index.html',
        {'object_list': object_list, 'page_obj':page_obj },
        )