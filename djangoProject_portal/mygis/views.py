from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from mygis.models import Articles


# Create your views here.
def home(request):
    # return HttpResponse("Hello world!")
    # return render(request, 'mygis/home.html')
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'mygis/home.html', context)

def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'mygis/article.html', {'article': article})

def about(request):
    return render(request, 'mygis/about.html')
