from django.shortcuts import render
from .models import Articles

def home(request):
    list_articles = Articles.objects.all()
    context = {"name": "Kondrich" , "list_articles":list_articles}
    template = "articles/home.html"
    return render(request, template, context)
