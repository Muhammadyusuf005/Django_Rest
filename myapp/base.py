import uuid
from django.db import models

class BaseModel(models.Model):
    """
    This model is base for all models.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    guid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey('myapp.Account',
                                   on_delete=models.CASCADE,
                                   null=True, blank=True,
                                   editable=False)

    class Meta:
        abstract = True