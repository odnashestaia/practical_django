"""
вывод постов пользователей
"""
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from discussions.models import *
from .forms import DiscussionCreateForms


class UserDiscussionListView(ListView):
    # модель пост в blog.model.py
    model = Discussion
    # выбор шаблона
    template_name = 'discussions/user_discussion.html'
    # имя к которому будем обращатся в шаблоне
    context_object_name = 'discussion_post_user_list'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Discussion.objects.filter(author=user).order_by('-date_created')

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        queryset = Discussion.objects.filter(author=user)
        context = super().get_context_data(**kwargs)
        context['blog_discussion_user_list'] = queryset.order_by('-date_created')

        return context


# class DiscussionCreateView(LoginRequiredMixin, CreateView):
#     model = Discussion
#     fields = ['title', 'content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


class DiscussionDetailView(DetailView):
    model = Discussion
    template_name = "discussions/discussion_detail.html"
    context_object_name = 'discussion_detail'


@login_required
def discussion_create(request):
    # проверка на POST запрос
    if request.method == 'POST':
        # Создадим экземпляр формы и заполним его данными запроса (укажем параметры)
        # Создадим форму для редактирования.
        form = DiscussionCreateForms(request.POST, request.FILES)  # данные POST для заполнения формы

        # проверка на валидность заполнения формы
        if form.is_valid():
            # созраняем данные из формы в оперативку для быстроты дальнейшего заполнения
            new_discussion = form.save(commit=False)
            # присваиваим дискусии автора
            new_discussion.author = request.user
            # сохранение в базу
            new_discussion.save()
            messages.success(request, 'Дискусия успешно сохранена')
            return redirect(new_discussion.get_absolute_url())
    else:
        # если поступит get запрос (или любой др), вернуть пустую форму.
        form = DiscussionCreateForms()
    return render(request=request, template_name='discussions/create_form.html', context={'form': form})
