# django imports
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    '''
    Inherited AbstractUser to add some user
    fields
    '''
    company_name = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=15)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def display_name(self):
        if self.first_name and self.last_name:
            name = "{} {}".format(self.first_name, self.last_name)
        else:
            name = self.username
        return name