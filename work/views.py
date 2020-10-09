from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from .models import Project, Category
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import AccessMixin


class IndexView(TemplateView):
    template_name='index.html'
    extra_context= {
        'title':'Main Page',
    }

class ProjectList(ListView):
    model = Project
    template_name = 'projects/list_projects.html'
    extra_context = {
        'title': 'Wszystkie projekty',
    }

class ProjectDetail(DetailView):

    model = Project
    template_name = 'projects/project_details.html'

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Project {self.object}',
        }
        context.update(kwargs)
        return super().get_context_data(**context)





class CategoryList(ListView):
    model = Category
    template_name = 'projects/list_categories.html'
    extra_context = {
        'title': 'Wszystkie kategorie',
    }

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['joanna@wloskowicz.pl'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('work:success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')