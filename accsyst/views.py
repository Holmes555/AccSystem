import subprocess

import pandas as pd
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.utils import timezone
from django.views.generic import View, FormView, ListView
from registration.backends.simple.views import RegistrationView

from .forms import *
from .models import *


class MyRegistrationView(RegistrationView):

    def get_success_url(self, user=None):
        return reverse('accsyst:index')


class CardFormView(FormView):
    template_name = 'accsystem/card_form.html'
    form_class = CardForm
    model = Card

    def post(self, request, *args, **kwargs):
        context_dict = {'form': self.form_class}
        card_form = self.form_class(data=request.POST)
        if card_form.is_valid():
            card = card_form.save(commit=False)
            card.save()
            return redirect(reverse('accsystem:card'))
        context_dict['form'] = card_form
        return render(request, self.template_name, context=context_dict)


class CardView(FormView):
    template_name = 'accsystem/card.html'
    model = UserProfile

    def get(self, request, *args, **kwargs):
        context_dict = {'username': kwargs['username']}
        try:
            user = User.objects.get(username=kwargs['username'])
        except User.DoesNotExist:
            return redirect(reverse('rast:index'))
        profile_user = self.model.objects.get_or_create(user=user)[0]
        context_dict['profile'] = profile_user
        return render(request, self.template_name, context=context_dict)

    def post(self, request, *args, **kwargs):
        return redirect(reverse('rast:register_profile'))


class WorkerListView(ListView):
    template_name = 'accsystem/worker_list.html'
    model = Worker


class WorkerView(View):
    template_name = 'accsystem/worker.html'
    model = Worker

    def get(self, request, *args, **kwargs):
        context_dict = {}
        worker_id = int(kwargs['job_id'])
        worker = None
        if worker_id:
            try:
                worker = self.model.objects.get(id=worker_id)
            except self.model.DoesNotExist:
                pass
            except ValueError:
                pass
            context_dict['worker'] = worker
        return render(request, self.template_name, context=context_dict)
    

class ReportListView(ListView):
    template_name = 'accsystem/report_list.html'
    model = Report


class ReportView(View):
    template_name = 'accsystem/report.html'
    model = Report

    def get(self, request, *args, **kwargs):
        context_dict = {}
        report_id = int(kwargs['job_id'])
        report = None
        if report_id:
            try:
                report = self.model.objects.get(id=report_id)
            except self.model.DoesNotExist:
                pass
            except ValueError:
                pass
            context_dict['report'] = report
        return render(request, self.template_name, context=context_dict)


class ReportFormView(FormView):
    template_name = 'accsystem/report_form.html'
    form_class = ReportForm
    model = Report
    
    def post(self, request, *args, **kwargs):
        context_dict = {'form': self.form_class}
        report_form = self.form_class(data=request.POST)
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.save()
            return redirect(reverse('accsystem:report'))
        context_dict['form'] = report_form
        return render(request, self.template_name, context=context_dict)
