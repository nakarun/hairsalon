from django.db import models
from hairsalon.models import Salon
from accounts.models import CustomerUser

import uuid


# Create your models here.

class StampManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_already_used=False).order_by('stamped_at')


class PointCard(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salon = models.ForeignKey(Salon, on_delete=models.PROTECT)
    vertical_cells_count = models.IntegerField()
    horizontal_cells_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.salon.name + ' : ポイントカード'

    class Meta:
        verbose_name = "ポイントカード"


class Stamp(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    pointcard = models.ForeignKey(PointCard, on_delete=models.PROTECT)
    stamped_at = models.DateTimeField()
    is_already_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    unused_objects = StampManager()

    def __str__(self):
        return self.customer.username + ':' + self.stamped_at.strftime('%Y/%m/%d')

    class Meta:
        verbose_name = "スタンプ"
