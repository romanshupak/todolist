from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
