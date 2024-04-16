import datetime
from django.utils import timezone
from django.contrib import admin
from .models import Article, Content


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "article_id",
        "article_title",
        "publish_date",
        "is_published_recently",
    )

    def is_published_recently(self, obj):
        return obj.publish_date >= timezone.now() - datetime.timedelta(days=1)

    is_published_recently.boolean = True  # 管理画面でアイコン表示
    is_published_recently.short_description = (
        "Published recently?"  # カラムのヘッダー名
    )


class ContentAdmin(admin.ModelAdmin):
    list_display = ("content_id", "article_id", "content_title", "content_order")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Content, ContentAdmin)
