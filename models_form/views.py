from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            create_author = form.cleaned_data
            create_author = form.save()
            create_author.save()
            # name = form.cleaned_data['name']
            # title = form.cleaned_data['title']
            # birthday = form.cleaned_data['birthday']
            return HttpResponseRedirect('author_detail')

    else:
        form = AuthorForm()

    return render(request, 'mform/author-form.html', {'form': form})


class AuthorListView(ListView):
    model = Author
    paginate_by = 3
    context_object_name = 'author_list'
    template_name = 'mform/author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author_detail'
    template_name = 'mform/author_detail.html'
