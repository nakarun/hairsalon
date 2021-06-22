from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from accounts.models import BaseUser
import uuid


# Create your models here.

class Salon(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "美容室"


class SalonStaff(BaseUser):
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)

    class Meta:
        verbose_name = "サロンスタッフ"


class News(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(null=True, blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    class Meta:
        verbose_name = "お知らせ投稿"
