from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, View

from playground.blog.models import Post, Category
from playground.blog.forms import PostForm


class PostList(TemplateView):
    template_name = 'blog/post_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)

        context['segregated'] = [
            [
                category,
                Post.objects.filter(category=category).order_by('-posted')
            ]
            for category in Category.objects.order_by('name')
        ]

        return context


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostCreate(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'blog/post_create.html', {'form': PostForm()})

    def post(self, *args, **kwargs):
        form = PostForm(self.request.POST)

        if not form.is_valid():
            return render(self.request, 'blog/post_create.html', {'form': form})

        post = form.save()
        post.author = self.request.user
        post.save()
        return redirect(reverse('post_detail', kwargs={'pk': post.pk}))


def post_detail_reverse(request, pk):
    post = Post.objects.get(pk=pk)
    post.text = post.text[::-1]
    return render(request, 'blog/post_detail.html', {'post': post})
