from django.db import models
from app_LR.models import User
# Create your models here.

# POST
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    post = models.TextField()
    liked = models.ManyToManyField(User, related_name="posts_liked")
    disliked = models.ManyToManyField(User, related_name="posts_disliked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments

# COMMENT
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Profile
class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    # image = models.ImageField(null=True)
    followed = models.ManyToManyField("self", related_name="followers")
    followers = models.ManyToManyField("self", related_name="following")