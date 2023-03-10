from django.db import models

TODO_STATUS_CHOICES = (
    ("todo", "Todo"),
    ("progress", "Progress"),
    ("blocked", "Blocked"),
    ("done", "Done"),
)

class Todo(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=TODO_STATUS_CHOICES)
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.title
