from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import View
from django.urls import reverse_lazy

from work.models import Project
from .models import Reviews


class AddReview(LoginRequiredMixin, CreateView):
    model = Reviews
    template_name = 'reviews/add.html'
    fields = ['title', 'content', 'grade']
    success_url = reverse_lazy('reviews:list-reviews')

    def get_context_data(self, **kwargs):
        context = {
            'title': f'Add your opinion "{self.project}"',
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    def get_project(self):
        project_id = self.kwargs.get('project_id')
        return get_object_or_404(Project, pk=project_id)

    def get(self, request, *args, **kwargs):
        self.project = self.get_project()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.project = self.get_project()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.project = self.project
        form.instance.state = 'draft'
        return super().form_valid(form)


class EditReview(UpdateView):
    model = Reviews
    pk_url_kwarg='review_id'
    template_name = 'reviews/edit.html'
    fields = ['title', 'content', 'grade']
    success_url = reverse_lazy('reviews:list-reviews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.book = self.object.book
        form.instance.state = 'draft'
        return super().form_valid(form)

class PublishReview(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id, state = 'draft', user=request.user)
        review.state = 'in_moderation'
        review.save()
        return redirect('reviews:list-reviews')


class ListReviews(ListView):
    template_name = 'reviews/list.html'
    extra_context = {
        'title': 'List of Your posts'
    }

    def get_queryset(self):
         return Reviews.objects.filter(user=self.request.user).order_by('state', 'pub_date')


class UnpublishReview(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Reviews, pk=review_id, state='in_moderation', user=request.user)
        review.state = 'draft'
        review.save()
        return redirect('reviews:list-reviews')


class ListReviews(LoginRequiredMixin, ListView):
    template_name = 'reviews/list.html'
    extra_context = {
        'title': 'List of Yours posts'
    }

    def get_queryset(self):
        return Reviews.objects.filter(user=self.request.user).order_by('state', 'pub_date')