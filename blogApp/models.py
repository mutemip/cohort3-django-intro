from django.db import models
from django.utils import timezone # Import timezone for DateTimeField
from django.contrib.auth.models import User # Import User model

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # If a user created the post is deleted, posts are deleted as well.ß

    # __str__() method returns how the Post is printed
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'post'