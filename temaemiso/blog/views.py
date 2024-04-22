from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("blog_home.html")  # テンプレートをロードする
    context = {
        "blog_title": "手前みそブログ",
        "topic_disp": True,
        "test_flag": False,
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))

def article(request, article_id:int = 1):
    template = loader.get_template("blog_articles.html")  # テンプレートをロードする
    context = {
        "blog_title": f"手前みそブログ({article_id})",
        "topic_disp": False,
        "test_flag": True,
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))