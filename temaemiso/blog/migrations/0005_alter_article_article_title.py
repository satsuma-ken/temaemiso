# Generated by Django 5.0.4 on 2024-04-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_article_article_title_alter_content_article_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(default='article_2024-04-20_172938', max_length=255),
        ),
    ]