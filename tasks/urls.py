from django.urls import path
from tasks.views import (
    index,
    TagsListView,
    CreateTaskView,
    CreateTagView,
    DeleteTagView,
    UpdateTagView,
    ToggleTaskStatusView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tasks-create/", CreateTaskView.as_view(), name="tasks-create"),
    path("tag-create/", CreateTagView.as_view(), name="tags-create"),
    path("tag-update/<int:pk>/", UpdateTagView.as_view(), name="tags-update"),
    path("tag-delete/<int:pk>/", DeleteTagView.as_view(), name="tags-delete"),
    path(
        "toggle-status/<int:pk>/",
        ToggleTaskStatusView.as_view(),
        name="toggle-status"
    ),


]

app_name = "tasks"
