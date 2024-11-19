from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

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
    success_url = reverse_lazy("tasks:index")


class CreateTagView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/tags_form.html"


class UpdateTagView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:index")
    template_name = "tasks/tags_form.html"


class DeleteTagView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tags_confirm_delete.html"
    success_url = reverse_lazy("tasks:index")


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        """Toggle the status of a task between done and not done."""
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("tasks:index")
