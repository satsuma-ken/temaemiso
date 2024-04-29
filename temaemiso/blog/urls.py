from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("article/<int:article_id>/", views.article, name="article"),
    path("article/test/", views.article_test, name="article_test"),
]