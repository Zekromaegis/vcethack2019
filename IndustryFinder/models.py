from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import jsonfield

#User.Student_set.all.0

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    academics = jsonfield.JSONField()
    sports = jsonfield.JSONField()
    technical = jsonfield.JSONField()
    social = models.IntegerField()
    
    def get_absolute_url(self):
        return reverse('IndustryFinder:details',kwargs={'pk': self.pk})
    #def get_success_url(self):
     #   return reverse('IndustryFinder:details', kwargs={'pk': self.pk})
    def __str__(self):
        return str(self.user.username) + " " + str(self.pk)