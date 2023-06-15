import django.contrib.messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms_app.forms import ContactForm
from django.contrib import messages


def contact_send(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            date_creation = form.cleaned_data['date_creation']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['lapunovn14@gmail.com']
            if cc_myself:
                recipients.append(message)
        else:
            messages.error(request, 'Error')

        try:
            send_mail(sender, message, cc_myself, recipients)
        except BadHeaderError:
            return HttpResponse('Неверный email')
        return redirect('sucsess')

    return render(request, 'forms_app/email.html', {'form': form})

