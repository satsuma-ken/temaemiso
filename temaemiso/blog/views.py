from django.http import HttpResponse
from django.template import loader, Template
from temaemiso.blog.models import Article


def index(request):
    template = loader.get_template("blog_home.html")  # テンプレートをロードする
    context = {
        "blog_title": "手前みそブログ",
        "topic_disp": True,
        "test_flag": False,
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))


def article(request, article_id: int = 1):
    template = loader.get_template("blog_articles.html")  # テンプレートをロードする
    disp_article = search_article_by_id(article_id=article_id)
    # print(disp_article.article_title)
    disp_article_title = disp_article.article_title
    # print(disp_article.article_overview)
    # print(disp_article.content_set.values_list("content", flat=True))
    disp_content_string = disp_article.content_set.values_list("content", flat=True)[0]
    # disp_content_html = Template(disp_content_string)
    context = {
        "blog_title": "手前みそブログ",
        "blog_content_title": f"「手前味噌ですが。。。**{disp_article_title}** です。。。」",
        "blog_content": disp_content_string,
        "topic_disp": False,
        "test_flag": True,
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))


def search_article_by_id(article_id: int = 1):
    try:
        article = Article.objects.get(pk=article_id)
        return article
    except Article.DoesNotExist:
        print("指定したIDの記事が見つかりませんでした。")
