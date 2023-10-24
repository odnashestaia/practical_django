"""
вывод постов пользователей
"""
import random

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from blog.forms import CommentForm
from blog.models import *


# COMPLETED: кончил
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


class UserPostListView(ListView):
    # модель пост в blog.model.py
    model = Post
    # выбор шаблона
    template_name = 'blog/user_post.html'
    # показывает сколько страниц показывать при пагинации
    paginate_by = 3
    # имя к которому будем обращатся в шаблоне
    context_object_name = 'blog_post_user_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_created')

    # def get_context_data(self, **kwargs):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Post.objects.filter(author=user).order_by('-date_created')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def saved_post_is_ajax(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    saved = False
    if post.save_posts.filter(id=request.user.id).exists():
        post.save_posts.remove(request.user)
        saved = False
    else:
        post.save_posts.add(request.user)
        saved = True
    context = {
        'post': post,
        'total_saved_post': post.total_save(),
        'saved': saved
    }

    if request.is_ajax():
        html = render_to_string('blog/save_section.html',
                                context, request=request)

        return JsonResponse({'form': html})


# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"
#     context_object_name = 'post_detail'

def post_detail_view(request, pk, slug):
    handel_page = get_object_or_404(Post, id=pk, slug=slug)

    total_comments = handel_page.comments_blog.all().filter(
        reply_comment=None).order_by('-id')
    total_comments2 = handel_page.comments_blog.all().order_by('-id')
    total_likes = handel_page.total_likes()
    total_save = handel_page.total_save()

    context = {}

    if request.method == 'POST':  # проверка сделан запрос
        comments_qs = None  # нету комментов под комментами
        # типо пусто или не пусто
        comments_form = CommentForm(request.POST or None)
        if comments_form.is_valid():  # если форма валидна
            form = request.POST.get('body_text')
            comment = Comment.objects.create(name_author=request.user, post=handel_page, body_text=form,
                                             reply_comment=comments_qs)
            comment.save()
            total_comments = handel_page.comments_blog.all().filter(
                reply_comment=None).order_by('-id')
    else:
        comments_form = CommentForm()

    like = False
    if handel_page.likes_post.filter(id=request.user.id).exists():
        like = True

    context['total_likes'] = total_likes
    context['like'] = like

    saved = False
    if handel_page.save_posts.filter(id=request.user.id).exists():
        saved = True

    context['total_save'] = total_save
    context['saved'] = saved

    context['comment_form'] = comments_form
    context['comments'] = total_comments
    context['post'] = handel_page

    if request.is_ajax():
        html = render_to_string('blog/comments.html', context)
        return JsonResponse({"form": html})

    return render(request, 'blog/post_detail.html', context)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post  # работа с моделью
    success_url = ('/')  # перенапровление после выполнения удаления
    template_name = 'blog/delete_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ проверка на юзера, то есть проверяем может ли этот юзер работать с записью """
        post = self.get_object()  # берем данные из модели post
        if self.request.user == post.author:  # сверяем автора поста и пользователя
            return True
        return False


class HomePostListViewAllUsers(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(HomePostListViewAllUsers, self).get_context_data()
        user = list(User.objects.exclude(pk=self.request.user.pk))
        if len(user) > 3:
            out = 3
        else:
            out = len(user)
        random_user = random.sample(user, out)
        context['random_users'] = random_user
        return context


@login_required
def all_save_view_post(request):
    user = request.user
    saved_post = user.save_posts.all()
    context = {'save_post': saved_post}
    return render(request, 'blog/saved_post.html', context)


@login_required
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('id'))
    like = False
    if post.likes_post.filter(id=request.user.id).exists():
        post.likes_post.remove(request.user)
        like = False
    else:
        post.likes_post.add(request.user)
        like = True

    contex = {
        'post': post,
        'total_likes': post.total_likes(),
        'like': like,
    }

    if request.is_ajax():
        html = render_to_string(
            'blog/like_selektion.html', contex, request=request)

    return JsonResponse({'form': html})
