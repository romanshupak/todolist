from django.urls import path
from . import views
from .views import TagsListView

urlpatterns = [
    path("", views.index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags-list")
]

app_name = "tasks"
