from statistics import mode
from django.db import models
from django.forms import UUIDField
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description  = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
