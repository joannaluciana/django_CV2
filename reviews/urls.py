from django.urls import path

from . import views


app_name = 'reviews'
urlpatterns = [
    path('<int:project_id>/add', views.AddReview.as_view(), name='add-project-review'),
    path('<int:project_id>/<int:review_id>/edit', views.EditReview.as_view(), name='edit-project-review'),
    path('<int:project_id>/<int:review_id>/publish', views.PublishReview.as_view(), name='publish-project-review'),
    path('list', views.ListReviews.as_view(), name='list-reviews'),
]