from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

import uuid


# Create your models here.

MENU_CATEGORY = (
    ('ct', 'カット'),
    ('cl', 'カラー'),
    ('tr', 'トリートメント'),
)


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


class Menu(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(choices=MENU_CATEGORY, max_length=2)
    note = models.TextField()

    class Meta:
        verbose_name = "メニュー"

    def __str__(self):
        return self.title


class MenuSet(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    note = models.TextField()

    class Meta:
        verbose_name = "セットメニュー"

    def __str__(self):
        return self.title


class MenuSetRelation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    set_menu = models.ForeignKey(MenuSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.menu.title + ' ---> ' + self.set_menu.title