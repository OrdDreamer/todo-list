from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Tag: {self.name}"


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.content[:50] + ('...' if len(self.content) > 50 else '')

    def __repr__(self):
        return f"Task: {self.content[:50] + ('...' if len(self.content) > 50 else '')}"
