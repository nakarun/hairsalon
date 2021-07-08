from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

from hairsalon.models import Salon


# Create your models here.

class BaseUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ベースユーザ"


class SalonStaff(BaseUser):
    salon = models.ForeignKey(Salon, related_name='staffs', on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    class Meta:
        verbose_name = "サロンスタッフ"


class CustomerUser(BaseUser):
    nick_name = models.CharField(verbose_name='ニックネーム', max_length=30)

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = "利用者"
