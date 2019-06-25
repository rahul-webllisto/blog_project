from django.shortcuts import render, redirect
from .models import Article
from .forms import *
# Create your views here.


def blog_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article_list.html', {'articles':articles})


def blog_detail(request,pk):
    article = Article.objects.get(pk=pk) 
    form = CreateCommentForm()   
    return render(request, 'article_detail.html', {'article':article, 'form': form})

def create_blog(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
    else:
        form = CreateArticleForm()
        return render(request, 'create_article.html', {'form': form})


def add_comment(request,pk):        
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = article
            comment.save()
            return redirect('blog-detail', article.pk)
    else:
        form = CreateCommentForm()
        return render(request, 'add_comment.html', {'form': form})
