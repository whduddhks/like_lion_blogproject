from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title=models.CharField (max_length=50)
    writer=models.CharField(max_length=50)
    body=models.TextField()
    user=models.ManyToManyField(User, blank=True)

    def summary(self):
        return self.body[:10]

class Comment(models.Model):
    writer=models.CharField(max_length=200)
    content=models.TextField()
    point=models.ForeignKey(Blog, on_delete=models.CASCADE)