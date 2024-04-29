from django.http import HttpResponse
from django.template import loader, Template
from temaemiso.blog.models import Article, Tag
from bs4 import BeautifulSoup

# 記事が見つからなかった時のとりあえず表示する記事ID
ERROR_ARTICLE_ID = 1


def index(request):
    template = loader.get_template("blog_home.html")  # テンプレートをロードする
    articles = search_article_by_new()
    disp_contents = []
    for article in articles[:3]:
        print(f"pk: {article.pk}")
        soup = BeautifulSoup(article.content_set.values_list("content", flat=True)[0])
        body_inner_html = soup.body.decode_contents()
        disp_contents.append({"pk": article.pk, "html": body_inner_html})
        # disp_contents.append(article.content_set.values_list("content", flat=True)[0])
        disp_tags = search_all_tags()
    context = {
        "is_home": True,
        "blog_title": "手前みそブログ",
        "topic_disp": True,
        "test_flag": False,
        "disp_contents": disp_contents,
        "articles": articles,
        "disp_tags": disp_tags,
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))


def article(request, article_id: int = 1):
    template = loader.get_template("blog_articles.html")  # テンプレートをロードする
    disp_article = search_article_by_id(article_id=article_id)
    disp_article_title = disp_article.article_title
    disp_article_overview = disp_article.article_overview
    disp_content_string = disp_article.content_set.values_list("content", flat=True)[0]
    section_list = make_section_list(disp_content_string)
    context = {
        "is_home": False,
        "blog_title": "手前みそブログ",
        "blog_content_title": disp_article_title,
        "blog_content": disp_content_string,
        "blog_overview": disp_article_overview,
        "topic_disp": False,
        "test_flag": False,
        "section_list": section_list,
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
        articles = Article.objects.get_articles_order_by_publish_date()
        return articles
    except Article.DoesNotExist:
        print("記事が見つかりませんでした。とりあえずの記事を表示します。")
        # ひとまずID=1の記事を返す
        article = Article.objects.get(pk=ERROR_ARTICLE_ID)
        return articles

def search_all_tags():
    try:
        tags = Tag.objects.all()
        return [tag.name for tag in tags]
    except Tag.DoesNotExist:
        print("tagsが見つかりませんでした。")

def make_section_list(html: BeautifulSoup) -> BeautifulSoup:
    soup = BeautifulSoup(html, 'html.parser')
    header_list = []
    header_2_list = soup.findAll('h2')
    for header_2 in header_2_list:
        header_list.append(header_2.get('id'))
    return header_list
