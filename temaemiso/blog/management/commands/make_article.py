from django.core.management.base import BaseCommand

from temaemiso.blog.models import Article, Content

class Command(BaseCommand):
    help = "Make_Article"

    def add_arguments(self, parser):
        """システムユーザの数を指定するオプション

        Args:
            parser : オプションを追加するためのparser
        """
        parser.add_argument(
            "--contents",
            type=int,
            help="Specify the amount of contents. The default amount of users will be 5.",
        )

    def handle(self, *args, **options):
        """記事を作成するカスタムコマンド"""
        contents = options["contents"]
        if not contents:
            contents = 5
        new_article = Article(
            article_title="test_article_title", article_overview="test_article_overview"
        )
        new_article.save()
        for i in range(1, contents + 1):
            new_content = Content(
                article_id=new_article,
                content_title="section_title",
                content_order=i,
                content_overview=f"content{i}_overview_1",
                content=f"""content{i}_content_2,
                content{i}_content_3,
                content{i}_content_4,
                content{i}_content_5,
                content{i}_content_6,
                """,
            )
            new_content.save()