from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Avg
from django.views.generic import (
    ListView,
    CreateView,
    )
from .models import Task, Standard, Guestalk
from .consts import ITEM_PER_PAGE

class ListTaskView(LoginRequiredMixin, ListView):
    template_name = 'regular/task_list.html'
    model = Task

class StandardTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_standard.html'
    model = Standard
    fields = ['title', 'zoom', 'user']

class GuestalkTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_guest_list.html'
    model = Guestalk
    fields = ['day', 'vol', 'guest', 'guest_url', 'theme', 'spreadsheet']
    paginate_by = ITEM_PER_PAGE

class CreateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_guest_create.html'
    model = Guestalk
    fields = ['title', 'day', 'vol', 'guest', 'guest_url', 'theme', 'comment', 'template', 'thumbnail', 'spreadsheet', 'zoom', 'user']

class UpdateTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_guest_update.html'
    model = Guestalk
    fields = ['title', 'day', 'vol', 'guest', 'guest_url', 'theme', 'comment', 'template', 'thumbnail', 'spreadsheet', 'zoom', 'user']

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