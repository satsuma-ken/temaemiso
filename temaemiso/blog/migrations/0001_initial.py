# Generated by Django 5.0.4 on 2024-04-16 11:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("created_by", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.CharField(max_length=255)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("article_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "publish_date",
                    models.DateTimeField(default=datetime.datetime(2099, 12, 31, 0, 0)),
                ),
                (
                    "expire_date",
                    models.DateTimeField(default=datetime.datetime(2099, 12, 31, 0, 0)),
                ),
            ],
            options={
                "db_table": "article",
            },
        ),
        migrations.CreateModel(
            name="Content",
            fields=[
                ("created_by", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_by", models.CharField(max_length=255)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("content_id", models.AutoField(primary_key=True, serialize=False)),
                ("content_order", models.SmallIntegerField()),
                ("content_title", models.CharField(max_length=100)),
                ("content_overview", models.CharField(max_length=255)),
                ("content", models.TextField()),
                (
                    "article_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="blog.article"
                    ),
                ),
            ],
            options={
                "db_table": "content",
            },
        ),
    ]