from django.urls import path
from . import views
from .views import contactView, successView


app_name= 'work'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectList.as_view(), name = 'list-projects'),
    path('categories/', views.CategoryList.as_view(), name= 'list-categories'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    ]
