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

class CoverView(TemplateView):
    template_name='cover_letter.html'
    extra_context= {
        'title':'Cover letter',
    }

class DownlView(TemplateView):
    template_name='downl_file.html'
    extra_context= {
        'title':'Download CV',
    }

class ProjectList(ListView):
    model = Project
    template_name = 'projects/list_projects.html'
    extra_context = {
        'title': 'Projects',
    }

class ProjectDetail(DetailView):

    model = Project
    template_name = 'projects/project_details.html'

    def get_success_url(self):
        return reverse ('projects:project-details', kwargs={'pk': self.object.pk})
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permision()
        self.object = self.get_object()
        # chcemy go uzyc wyzej w get
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object
        self.grade = form.save()
        return super().form_valid(form)

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


def get_context_data (self,**kwargs):
        context = {'title':f'Project {self.object.name}',
        # SELECT AVG('grade') AS AVARAGE, COUNT ('grade')
        # AS COUNT FROM grades WHERE book_id=???
        # AGREGACJA liczy wprost - ANOTACJA doloaczy funkcje do kazdego obiektu
        'avg_grades': self.object.grade_set.aggregate(average = Avg('grade'),
        count = Count('grade')),
        }

        context.update(kwargs)

        return super().get_context_data(**context)