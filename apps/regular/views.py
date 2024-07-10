from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Avg
from django.views.generic import (
    ListView,
    FormView,
    )
from .models import Task, Standard, Guestalk

class ListTaskView(LoginRequiredMixin, ListView):
    template_name = '/templates/regular/task_list.html'
    model = Task

class StandardTaskView(LoginRequiredMixin, FormView):
    template_name = '/templates/regular/task_standard.html'
    model = Standard

class GuestalkTaskView(LoginRequiredMixin, FormView):
    template_name = '/templates/regular/task_guestalk.html'
    model = Guestalk