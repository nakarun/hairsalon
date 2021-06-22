from django.db import models
from hairsalon.models import Salon
from accounts.models import BaseUser

import uuid


# Create your models here.

class CustomerUser(BaseUser):
    nick_name = models.CharField(verbose_name='ニックネーム', max_length=30)

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = "カスタマー"


class SalonPointCard(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salon = models.ForeignKey(Salon, on_delete=models.PROTECT)
    max_stamp = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.salon.name + ' : ポイントカード'

    class Meta:
        verbose_name = "ポイントカード"


class Appointment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    appointment_at = models.DateTimeField()

    def __str__(self):
        return self.customer + '' + self.appointment_at

    class Meta:
        verbose_name = "予約"
