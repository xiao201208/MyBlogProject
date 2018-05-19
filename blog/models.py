# coding:utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_time = models.DateField('创建时间', default=timezone.now)
	modified_time = models.DateField('更新时间', auto_now=True)
	excerpt = models.CharField(max_length=200, blank=True)

	category = models.ForeignKey(Category)
	tags = models.ManyToManyField(Tag,blank=True)
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'pk': self.pk})
