from django.shortcuts import get_object_or_404, render

from .models import Group, Post

POSTS_ON_SCREEN = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:POSTS_ON_SCREEN]
    text = 'Последние обновления на сайте'
    context = {
        'title': text,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:POSTS_ON_SCREEN]
    template = 'posts/group_list.html'
    text = f'Записи сообщества {group.title}'
    context = {
        'group': group,
        'posts': posts,
        'title': text,
    }
    return render(request, template, context)
