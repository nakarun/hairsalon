from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class BaseUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ベースユーザ"
