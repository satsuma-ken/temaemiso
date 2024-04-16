# Generated by Django 5.0.4 on 2024-04-16 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_article_article_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="article_overview",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="article",
            name="article_title",
            field=models.CharField(default="article_2024-04-16_211004", max_length=255),
        ),
        migrations.AlterField(
            model_name="content",
            name="content",
            field=models.TextField(default=""),
        ),
    ]
