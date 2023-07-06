from forms_app.forms import ContactForm
import pytest
from django import forms
import datetime

# переменные для проверки максимального числа (странная проверка, хуй знает где пригодится
max_length_gt_100 = 'n' * 101
max_length_gt_99 = 'n' * 99
max_length_gt_555 = 'n' * 555
max_length_gt_499 = 'n' * 499



# pytest --tb=native - терминалтьная комманда, pycharьовский тест хуйня

# мы подготавливаем что тестируем и данные

#  subject, message, sender, cc_myself, validity
@pytest.mark.parametrize(
    'date_creation, valid_date',
    # ввод данных для тестирования
    [  # первый тест идеально работающий для проверки pytest
        (datetime.date.today(), True),
        ('2023-06-30', False),
        ('2024-07-30', False),

        ('', False),
        (None, False),
    ]
)
@pytest.mark.parametrize(
    'subject, valid_subject',
    # ввод данных для тестирования
    [  # первый тест идеально работающий для проверки pytest
        ('Ghbdtn', True),
        (max_length_gt_100, False),
        (max_length_gt_99, True),
        ('', False),
    ]
)
@pytest.mark.parametrize(
    'message, valid_message',
    # ввод данных для тестирования
    [  # первый тест идеально работающий для проверки pytest
        ('myjuj ntrcns', True),
        (max_length_gt_555, False),
        (max_length_gt_499, True),
        ('', False),
    ]
)
@pytest.mark.parametrize(
    'sender, valid_sender',
    # ввод данных для тестирования
    [  # первый тест идеально работающий для проверки pytest
        ('testA@gmail.com', True),
        ('testAgmail.com', False),
        ('testA@', False),
    ]
)
@pytest.mark.parametrize(
    'cc_myself, valid_cc',
    # ввод данных для тестирования
    [  # первый тест идеально работающий для проверки pytest
        ('', True),
        # ('dasdfasd', False),
        # ('2023-07-30',)
    ]
)
def test_valid_contact_form(date_creation, subject, message, sender, cc_myself, valid_date, valid_sender,
                            valid_message, valid_subject, valid_cc):
    form = ContactForm(data={
        'date_creation': date_creation,
        'subject': subject,
        'message': message,
        'sender': sender,
        'cc_myself': cc_myself
    })

    e = form.errors.as_data()
    print(e)

    assert form.is_valid() is (valid_subject and valid_message and valid_sender and valid_date and valid_cc)
