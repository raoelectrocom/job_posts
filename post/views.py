# django imports
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

# util imports
from post.models import JobPost


class JobPostListView(ListView):
    '''
    View class to list job posts
    '''
    model = JobPost


class MyJobPostListView(ListView):
    '''
    View class to list login recruiter 
    job posts
    '''

    def get_queryset(self):
        return JobPost.objects.filter(recruiter=self.request.user)


class JobPostDetails(DetailView):
    '''
    View class for Job post detail
    page
    '''
    model = JobPost


class JobPostCreate(CreateView):
    '''
    View class to create job post
    '''
    model = JobPost
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.recruiter = self.request.user
        self.object.save()
        return super().form_valid(form)


class JobPostUpdate(UpdateView):
    '''
    View class to update job post
    '''
    model = JobPost
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save(commit=False)
        self.object.recruiter = self.request.user
        self.object.save()
        return super().form_valid(form)


class JobPostDeleteView(DeleteView):
    '''
    View class to delete job post
    '''
    model = JobPost
    success_url = reverse_lazy('homepage')