# Generated by Django 5.0.4 on 2024-04-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_alter_article_article_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(default='article_2024-04-20_212710', max_length=255),
        ),
    ]
