from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid

# Create your models here.

class TimeStampUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)

    class Meta:
        abstract =True

