from django.shortcuts import render

from tasks.models import Task


def index(request):
    """View function for the home page of the site."""
    tasks = Task.objects.all()

    context = {"tasks": tasks}
    return render(request, "tasks/index.html", context=context)
