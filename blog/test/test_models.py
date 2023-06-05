import pytest
from django.contrib.auth.models import User

from blog.models import Post


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('user', 'user@mail.com', 'password')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_model_create():
    article = Post.objects.create(title='article1', content='sdfsdfsdfsdf', slug='qwdqwdqwdqw')
    assert article.title == 'article1'
    assert article.content == 'sdfsdfsdfsdf'
    assert article.slug == 'qwdqwdqwdqw'
