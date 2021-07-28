import uuid

from django.db import models

from question.models import Question

class Option(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.TextField(max_length=2500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> None:
        return f"<Option: {self.id}>"