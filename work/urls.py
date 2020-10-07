from django.urls import path
from . import views


app_name= 'work'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectList.as_view(), name = 'list-projects'),
    path('categories/', views.CategoryList.as_view(), name= 'list-categories'),

    ]
