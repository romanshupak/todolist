from django.urls import path
from tasks.views import (
    index,
    TagsListView,
    CreateTaskView,
    UpdateTaskView,
    DeleteTaskView,
    CreateTagView,
    DeleteTagView,
    UpdateTagView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tasks-create/", CreateTaskView.as_view(), name="tasks-create"),
    path("tasks-update/<int:pk>/", UpdateTaskView.as_view(), name="tasks-update"),
    path("tasks-delete/<int:pk>/", DeleteTaskView.as_view(), name="tasks-delete"),
    path("tag-create/", CreateTagView.as_view(), name="tags-create"),
    path("tag-update/<int:pk>/", UpdateTagView.as_view(), name="tags-update"),
    path("tag-delete/<int:pk>/", DeleteTagView.as_view(), name="tags-delete"),


]

app_name = "tasks"
