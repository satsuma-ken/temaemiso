from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("blog_base.html")  # テンプレートをロードする
    context = {
        "blog_title": "手前みそ",
    }  # テンプレートに当てはめる値
    # HTTPレスポンスとして返却
    return HttpResponse(template.render(context, request))
