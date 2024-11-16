from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from tasks.models import Task, Tag


def index(request):
    """View function for the home page of the site."""
    tasks = Task.objects.all()

    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context=context)


class TagsListView(generic.ListView):
    model = Tag
    template_name = "tasks/tags_list.html"


class CreateTaskView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/tasks_form.html"


class UpdateTaskView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/tasks_form.html"


class DeleteTaskView(generic.DeleteView):
    model = Task
    template_name = "tasks/tasks_confirm_delete.html"
    success_url = "tasks/tasks_form.html"

