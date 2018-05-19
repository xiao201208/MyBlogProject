from django.shortcuts import render, get_object_or_404
from .models import Article, Category
import markdown


def index(request):
    post_list = Article.objects.all().order_by('-created_time')
    return render(request, 'blog/article.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Article.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/article.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Article.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/article.html', context={'post_list': post_list})
