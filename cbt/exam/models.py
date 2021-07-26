from cbt.cbtuser.models import CBTUser
import uuid


from django.db import models


from cbtuser.models import CBTUser


class Exam(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(max_length=500, blank=False, null=False)
    description = models.TextField(max_length=1500, blank=False, null=False)
    exam_manager = models.ForeignKey(CBTUser, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.title) + str(self.exam_manager)
        
