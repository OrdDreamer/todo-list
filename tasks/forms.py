from django import forms
from .models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 3}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
