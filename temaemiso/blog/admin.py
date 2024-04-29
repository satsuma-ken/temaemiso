import datetime
from django.utils import timezone
from django.contrib import admin
from .models import Article, Content, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "article_id",
        "article_title",
        "publish_date",
        "is_published_recently",
        "tags",
    )
    filter_horizontal = ("tags",)

    def is_published_recently(self, obj):
        return obj.publish_date >= timezone.now() - datetime.timedelta(days=1)

    def tags(self, obj):
        return ",".join([x.name for x in obj.tags.all()])

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tags":
            kwargs["queryset"] = Tag.objects.order_by("name")
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    is_published_recently.boolean = True  # 管理画面でアイコン表示
    is_published_recently.short_description = (
        "Published recently?"  # カラムのヘッダー名
    )


class ContentAdmin(admin.ModelAdmin):
    list_display = ("content_id", "article_id", "content_title", "content_order")


admin.site.register(Article, ArticleAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Tag, TagAdmin)
