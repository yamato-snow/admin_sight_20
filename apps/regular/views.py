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

class GuestalkTaskView(LoginRequiredMixin, CreateView):
    template_name = 'regular/task_guestalk.html'
    model = Guestalk

def index_view(request):
    return render(
        request,
        'regular/index.html',
        )