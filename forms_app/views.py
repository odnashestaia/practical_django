import django.contrib.messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms_app.forms import ContactForm
from django.contrib import messages


def contact_send(request):
    # проверка на post запрос
    if request.method == 'POST':
        # если приходит post запрос, то форма заполняется
        form = ContactForm(request.POST, request.FILES)  # request.POST - обработка post запроса
        # request.FILES- обработка файлов не объяснил
        if form.is_valid():  # проверка на валидность формы для дольнейшего заполнения
            # добавление в форму данные
            date_creation = form.cleaned_data['date_creation']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['lapunovn14@gmail.com']  # почта откуда отправляется сообщение
            if cc_myself:  # проверка на добавления на рассылку
                recipients.append(message)
                try:
                    send_mail(subject, message, sender, recipients)  # отправка сообщений
                except BadHeaderError:
                    return HttpResponse('Неверный email')  # вывод ошибки
                # return redirect('success')  # переправляем дпользователя на другую страницу
                form = ContactForm()
                messages.success(request, 'Сообщение отправлено!')
        else:  # вывод ошибок
            messages.error(request, 'Error')
    else:
        # выдается пустая форма если это get запрос или какой-либо еще
        form = ContactForm()

    return render(request, 'forms_app/email.html', {'form': form})  # вывод формы в html
