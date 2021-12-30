# django imports
from django.db import models
from django.urls import reverse

# django third party imports
from tinymce.models import HTMLField

# util imports
from user.models import User


class JobPost(models.Model):
    title=models.CharField(max_length=255)
    recruiter= models.ForeignKey(User, on_delete=models.CASCADE)
    content=HTMLField()
    image = models.ImageField(upload_to="uploads")
    dateTime=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self): # new
        return reverse('job_detail', args=[str(self.id)])
    
    def __str__(self):
        return str(self.recruiter) +  " Post Title: " + self.title