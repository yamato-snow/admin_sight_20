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

class ListTaskView(LoginRequiredMixin, ListView):
    template_name = 'regular/task_list.html'
    model = Task

class StandardTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_standard.html'
    model = Standard
    fields = ['title', 'zoom', 'user']

class GuestalkTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_guestalk.html'
    model = Guestalk
    fields = ['title', 'day', 'vol', 'guest', 'guest_url', 'theme', 'comment', 'template', 'thumbnail', 'spreadsheet', 'zoom', 'user']

def index_view(request):
    task_list = Task.objects.all()
    standard_list = Standard.objects.all()
    guestalk_list = Guestalk.objects.all()
    
    paginator_task = Paginator(task_list, 10)  # 10 items per page
    paginator_standard = Paginator(standard_list, 10)  # 10 items per page
    paginator_guestalk = Paginator(guestalk_list, 10)  # 10 items per page
    
    page_number_task = request.GET.get('task_page')
    page_number_standard = request.GET.get('standard_page')
    page_number_guestalk = request.GET.get('guestalk_page')
    
    page_obj_task = paginator_task.get_page(page_number_task)
    page_obj_standard = paginator_standard.get_page(page_number_standard)
    page_obj_guestalk = paginator_guestalk.get_page(page_number_guestalk)
    
    context = {
        'page_obj_task': page_obj_task,
        'page_obj_standard': page_obj_standard,
        'page_obj_guestalk': page_obj_guestalk,
    }
    
    return render(request, 'regular/index.html', context)