from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
                                  ListView,
                                  TemplateView,
                                  FormView,
                                  View
                                )


from projects.models import Project, ProjectAssignment
from .models import TaskLog, Task
from .forms import TaskForm


class TaskListView(LoginRequiredMixin, TemplateView):
    """List of task by project
    """

    template_name = "timetracker/employee/tasks_list.html"

    def get_context_data(self, **kwargs):
        project = Project.objects.get(id=self.kwargs['project_id'])
        tasks = Task.objects.filter(member__project=project, member__employee=self.request.user)
        kwargs['tasks'] = tasks
        kwargs['project'] = project
        kwargs['form'] = TaskForm()
        return kwargs


class TaskLogListView(LoginRequiredMixin, ListView):
    """List of log per task
    """
    template_name = "timetracker/employee/taskslog_list.html"

    def get_queryset(self):
        queryset = TaskLog.objects.filter(task__id=self.kwargs['task_id'], task__member__employee=self.request.user)
        return queryset


class TaskCreateFormView(LoginRequiredMixin, FormView):
    """Create task
    """

    form_class = TaskForm

    def get_success_url(self):
        return reverse('project_task_list', kwargs={'project_id': self.kwargs['project_id']})

    def form_valid(self, form):
        project = Project.objects.get(id=self.kwargs['project_id'])
        assignee = ProjectAssignment.objects.get(project=project, employee=self.request.user)
        self.object = form.save(commit=False)
        self.object.member = assignee
        self.object.save()
        return super(TaskCreateFormView, self).form_valid(form)


class TaskDeleteView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        project_id = kwargs['project_id']
        task_id = kwargs['task_id']
        Task.objects.get(id=task_id, member__employee=self.request.user).delete()
        return HttpResponseRedirect(reverse('project_task_list', kwargs={'project_id': project_id}))


class TaskTimeInView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        project_id = kwargs['project_id']
        task_id = kwargs['task_id']
        task = Task.objects.get(id=task_id, member__employee=self.request.user)
        task.time_in()
        return HttpResponseRedirect(reverse('project_task_list', kwargs={'project_id': project_id}))


class TaskTimeOutView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        project_id = kwargs['project_id']
        task_id = kwargs['task_id']
        task = Task.objects.get(id=task_id, member__employee=self.request.user)
        task.time_out()
        return HttpResponseRedirect(reverse('project_task_list', kwargs={'project_id': project_id}))
