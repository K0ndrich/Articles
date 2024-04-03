from typing import Any
from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView

# def home(request):
#     list_articles = Articles.objects.all()
#     context = {"name": "Kondrich", "list_articles": list_articles}
#     template = "articles/index.html"
#     return render(request, template, context)


class HomeListView(ListView):
    model = Articles
    template_name = "articles/index.html"
    context_object_name = "list_articles"


# def detail_page(request, id):
#     get_article = Articles.objects.get(id=id)
#     context = {"get_article": get_article}
#     template = "articles/detail.html"
#     return render(request, template, context)


class HomeDetailView(DetailView):
    model = Articles
    template_name = "articles/detail.html"
    context_object_name = "get_article"


def edit_page(request):
    context = {}
    template = "articles/edit_page.html"
    return render(request , template , context)
