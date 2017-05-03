from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Projects, WorkDiary
from . forms import WorkDiaryForm


class ProjectView(LoginRequiredMixin, TemplateView):

    model = Projects
    template_name = 'project/projects.html'

    def get(self, request, *args, **kwargs):
        project = Projects.objects.all().order_by('-date')
        ctx_data = {
            'projects': project,
        }
        return render(self.request, self.template_name, ctx_data)


class WorkDiaryView(TemplateView):

    form_class = WorkDiaryForm
    model = WorkDiary
    template_name = 'project/work_diary.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(self.request, self.template_name, {'form': form})


class Reports(TemplateView):

    template_name = 'project/work_detail.html'

    def get(self, request, *args, **kwargs):
        work = WorkDiary.objects.all().order_by('-date')
        return render(request, self.template_name, {'work': work})