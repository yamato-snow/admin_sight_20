from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Avg
from django.views.generic import (
    ListView,
    FormView,
    CreateView,
    UpdateView,
    )
from .models import Task, Login, Standard, Guestalk

class ListTaskView(LoginRequiredMixin, ListView):
    template_name = '/templates/regular/task_list.html'
    model = Task

class LoginTaskView(LoginRequiredMixin, FormView):
    template_name = '/templates/regular/task_login.html'
    model = Login

class RegTaskView(LoginRequiredMixin, CreateView):
    template_name = '/templates/regular/task_reg.html'
    model = Login

class PasswordTaskView(LoginRequiredMixin, UpdateView):
    template_name = '/templates/regular/task_password.html'
    model = Login

class StandardTaskView(LoginRequiredMixin, UpdateView):
    template_name = '/templates/regular/task_standard.html'
    model = Standard

class GuestalkTaskView(LoginRequiredMixin, UpdateView):
    template_name = '/templates/regular/task_guestalk.html'
    model = Guestalk