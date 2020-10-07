from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Project, Category

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


class CategoryList(ListView):
    model = Category
    template_name = 'projects/list_categories.html'
    extra_context = {
        'title': 'Wszystkie kategorie',
    }