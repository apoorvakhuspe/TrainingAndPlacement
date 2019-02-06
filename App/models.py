from __future__ import unicode_literals
from django.db import models

user_type = [('student',"Student"),('teacher',"Teacher")]
class person(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25, blank=False)
    email = models.CharField(max_length=50)
    user_type = models.CharField(choices=user_type,max_length=25)

    def __str__(self):
        return self.username+" "+self.email+" "+self.user_type

# Create your models here.
