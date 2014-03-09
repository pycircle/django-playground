from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from playground.blog.models import Post, Category
from playground.blog.forms import PostForm


def post_list(request):
    categories = Category.objects.order_by("name")
    segregated = []
    for category in categories:
        posts = Post.objects.filter(category=category).order_by('-posted')
        segregated.append([category, posts])
    return render(request, 'blog/post_list.html', {'segregated': segregated})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect(reverse('post_detail', kwargs={'pk': post.pk}))

    else:
        form = PostForm()

    return render(request, 'blog/post_create.html', {'form': form})


def post_detail_reverse(request, pk):
    post = Post.objects.get(pk=pk)
    post.text = post.text[::-1]
    return render(request, 'blog/post_detail.html', {'post': post})
