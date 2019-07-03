from django.shortcuts import render, redirect
from .models import Article
from .forms import *
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



def blog_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'article_list.html', {'articles':articles})



@api_view(['GET', 'POST'])
def blog_list_api(request):
    
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)        
        for article in range(len(serializer.data)):            
            del serializer.data[article]['comments']
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

        
        
@api_view(['GET', 'PUT', 'DELETE'])
def blog_detail_api(request,pk):
    """
    Retrieve, update or delete a article.
    """
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)        
        return Response(serializer.data)

    elif request.method == 'PUT':        
        serializer = ArticleSerializer(article, data=request.data, partial=True)        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=204)



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



@api_view(['POST'])
def add_comment_api(request,pk,):
    """
    create, update or delete a comment.
    """
    try:
        article = Article.objects.get(pk=pk)        
    except Article.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'POST':                
        serializer = CommentSerializer(data=request.data)        
        if serializer.is_valid():
            serializer.save(post=article)            
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['PUT', 'DELETE'])
def add_comment_api(request,pk,):
    pass