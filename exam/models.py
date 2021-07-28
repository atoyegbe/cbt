import uuid

from django.db import models

# try:
#     import sys
#     temp = sys.path
#     sys.path.append("..")
#     from cbtuser.models import CBTUser
# except Exception("Could not import CBTUser"):
#     sys.exit()


class Exam(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(max_length=500, blank=False, null=False)
    description = models.TextField(max_length=1500, blank=False, null=False)
    exam_code = models.CharField(max_length=15, blank=False, null=False, default="NULL")
    exam_manager = models.ForeignKey("cbtuser.CBTUser", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f" {self.title} - {self.exam_manager}"