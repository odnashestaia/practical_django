# How tests works

`
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
`

## То что начинаеться с `@` это подключение к базе 

## test_user_create - это проверка модели на создание пользователя 

## test_model_create - проверка на создание моделей 

# У меня не получилось сделать проверку manytomany и forenkey надо найти способ