# Generated by Django 3.2 on 2021-07-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pointcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stamp',
            name='stamped_at',
            field=models.DateField(),
        ),
    ]
