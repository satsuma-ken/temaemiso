# Generated by Django 5.0.4 on 2024-04-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(default='article_2024-04-20_175819', max_length=255),
        ),
    ]