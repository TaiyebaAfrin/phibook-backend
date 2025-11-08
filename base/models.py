from django.db import models
from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     username = models.CharField(max_length=50, unique=True, primary_key=True)
#     bio = models.CharField(max_length=500, blank=True, default='')
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
#     followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

#     def __str__(self):
#         return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    bio = models.CharField(max_length=500, blank=True, default='')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    
    # Add the missing subscription_plan field
    subscription_plan = models.CharField(
        max_length=100, 
        default='free',  # Set default value
        blank=True,
        null=False
    )

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(MyUser, related_name='post_likes', blank=True)
    
    # Temporary field to match database
    post_type = models.CharField(max_length=20, default='text', blank=True)
    
    def __str__(self):
        return f"Post by {self.user.username} - {self.created_at}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on post {self.post.id}"