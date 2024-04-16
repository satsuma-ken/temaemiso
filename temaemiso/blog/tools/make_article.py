from temaemiso.blog.models import Article, Content


def make_article():
    new_article = Article(
        article_title="test_article_title", article_overview="test_article_overview"
    )
    new_article.save()
    for i in range(5):
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
