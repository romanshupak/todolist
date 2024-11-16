from django.urls import path
from . import views
from .views import TagsListView, CreateTaskView

urlpatterns = [
    path("", views.index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tasks-create/", views.CreateTaskView.as_view(), name="tasks-create"),

]

app_name = "tasks"
