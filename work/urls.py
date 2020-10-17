from django.urls import path
from . import views
from .views import contactView, successView


app_name= 'work'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectList.as_view(), name = 'list-projects'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name= 'project-details'),
    path('categories/', views.CategoryList.as_view(), name= 'list-categories'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('download/', views.DownlView.as_view(), name='downl_file'),
    path('cover/', views.CoverView.as_view(), name='cover_view'),
    ]
