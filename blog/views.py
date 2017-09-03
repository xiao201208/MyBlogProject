from django.shortcuts import render, get_object_or_404
from .models import Article
import markdown

def index(request):
	post_list = Article.objects.all().order_by('-created_time')
	return render(request,'blog/article.html',context={'post_list':post_list})


def detail(request,pk):
	post = get_object_or_404(Article, pk=pk)
	post.body = markdown.markdown(post.body, extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc'
	])
	return render(request, 'blog/detail.html', context={'post':post})


