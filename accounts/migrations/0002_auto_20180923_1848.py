# -*- coding: utf-8 -*-
# Generated by Django 2.1 on 2018-09-24 01:48
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="user", name="id"),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
