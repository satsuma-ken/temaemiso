from django.http import HttpResponse
from django.template import loader, Template
from temaemiso.blog.models import Article

# 記事が見つからなかった時のとりあえず表示する記事ID
ERROR_ARTICLE_ID = 1


def index(request):
    articles = search_article_by_new()
    for article in articles:
        print(article)
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
    disp_article_title = disp_article.article_title
    disp_content_string = disp_article.content_set.values_list("content", flat=True)[0]
    context = {
        "blog_title": "手前みそブログ",
        "blog_content_title": disp_article_title,
        "blog_content": disp_content_string,
        "topic_disp": False,
        "test_flag": False,
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))


def article_test(request):
    template = loader.get_template("blog_articles.html")  # テンプレートをロードする
    disp_article_title = "test表示です"
    disp_content_string = "test表示です"
    context = {
        "blog_title": "手前みそブログ",
        "blog_content_title": disp_article_title,
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
        print("記事が見つかりませんでした。とりあえずの記事を表示します。")
        # ひとまずID=1の記事を返す
        article = Article.objects.get(pk=ERROR_ARTICLE_ID)
        return article


def search_article_by_new():
    try:
        articles = Article.objects.get_latest_three_articles()
        return articles
    except Article.DoesNotExist:
        print("記事が見つかりませんでした。とりあえずの記事を表示します。")
        # ひとまずID=1の記事を返す
        article = Article.objects.get(pk=ERROR_ARTICLE_ID)
        return articles
