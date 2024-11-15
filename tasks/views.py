from django.shortcuts import render
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

