from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    class Meta:
        # マイグレーション時にテーブルを作成しないModelは以下のオプションが必要
        abstract = True

    # 以下、共通カラム
    created_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)


class Article(BaseModel):
    DEFAULT_DATETIME = datetime(2099, 12, 31, 0, 0, 0)
    datetime_now = datetime.now()

    class Meta:
        db_table = "article"

    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=255, default=f"article_{datetime_now:%Y-%m-%d_%H%M%S}")
    article_overview = models.TextField(default="")
    publish_date = models.DateTimeField(default=DEFAULT_DATETIME)
    expire_date = models.DateTimeField(default=DEFAULT_DATETIME)


class Content(BaseModel):
    class Meta:
        db_table = "content"

    article_id = models.ForeignKey(
        Article,
        on_delete=models.PROTECT,
    )
    content_id = models.AutoField(primary_key=True)
    content_order = models.SmallIntegerField()
    content_title = models.CharField(max_length=100)
    content_overview = models.TextField(max_length=255)
    content = models.TextField(default="")
