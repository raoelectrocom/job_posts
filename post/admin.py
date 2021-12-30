from django.contrib import admin

# Register your models here.
from post.models import JobPost

admin.site.register(JobPost)