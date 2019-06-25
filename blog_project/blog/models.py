from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
 
class Article(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    # author = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def approve(self):
        self.is_approved = True
        self.save()

    def __str__(self):
        return self.text