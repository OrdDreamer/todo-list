from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)

from .forms import TaskForm, TagForm
from .models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = "tasks"
    paginate_by = 20

    def get_queryset(self):
        queryset = Task.objects.all().prefetch_related("tags")
        queryset = queryset.order_by("is_done", "-created_at")
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_page"] = "active"
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_page"] = "active"
        return context


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_page"] = "active"
        return context


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task_page"] = "active"
        return context


class TaskToggleView(View):
    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("tasks:task_list")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_page"] = "active"
        return context


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_page"] = "active"
        return context


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_page"] = "active"
        return context


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_page"] = "active"
        return context
