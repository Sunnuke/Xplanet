from django.db import models
from app_LR.models import User
# Create your models here.


# Profile
class Profile(models.Model):
    name = models.CharField(max_length=30, default="New Comer")
    bio  = models.TextField(default="This human is a New Comer! ...or is just to lazy to leave a comment in their Bio!")
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE)
    # image = models.ImageField(null=True)
    following = models.ManyToManyField('self', related_name="you_followed", symmetrical=False)
    followers = models.ManyToManyField('self', related_name="who_follows", symmetrical=False)
    # posts
    # posts_liked
    # posts_disliked
    # profile_comments

# POST
class Post(models.Model):
    title = models.CharField(max_length=30, null=True)
    profile = models.ForeignKey(Profile, related_name="posts", on_delete=models.CASCADE, null=True)
    post = models.TextField()
    liked = models.ManyToManyField(Profile, related_name="posts_liked")
    disliked = models.ManyToManyField(Profile, related_name="posts_disliked")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comments

# COMMENT
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name="profile_comments", on_delete=models.CASCADE, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

