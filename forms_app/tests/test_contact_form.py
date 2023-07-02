from forms_app.forms import ContactForm
import pytest
from django import forms
import datetime

# pytest --tb=native - терминалтьная комманда, pycharьовский тест хуйня

# мы подготавливаем что тестируем и данные
@pytest.mark.parametrize(
    'date_creation, subject, message, sender, cc_myself, validity',
    # ввод данных для тестирования
    [  # первый тест идеально работающий для проверки pytest
        ('2023-06-30', 'djghjc xktyf d rjvyfnt', 'jy ckbirjv ,jkmijq lkz yfc ltcznths[', 'django@mail.com', 'cc_myself',
         True),
        # date_creation дата на будующие число не работает
        ('2023-07-30', 'djghjc xktyf d rjvyfnt', 'jy ckbirjv ,jkmijq lkz yfc ltcznths[', 'django@mail.com', 'cc_myself',
         True),
        # в почте нет собаки
        ('2023-07-30', 'djghjc xktyf d rjvyfnt', 'jy ckbirjv ,jkmijq lkz yfc ltcznths[', 'djangomail.com', 'cc_myself',
         True),
    ]
)
def test_valid_contact_form(date_creation, subject, message, sender, cc_myself, validity):
    form = ContactForm(data={
        'date_creation': date_creation,
        'subject': subject,
        'message': message,
        'sender': sender,
        'cc_myself': cc_myself
    })

    # e = form.errors()
    # print(e)

    assert form.is_valid() is validity
