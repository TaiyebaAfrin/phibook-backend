# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     username = models.CharField(max_length=50, unique=True, primary_key=True)
#     bio = models.CharField(max_length=500)
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
#     followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

#     def __str__(self):
#         return self.username

# class Post(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
#     description = models.CharField(max_length=400)
#     created_at = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(MyUser, related_name='post_likes', blank=True)

#     def __str__(self):
#         return f"Post by {self.user.username}"

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')
#     text = models.CharField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"Comment by {self.user.username} on {self.post}"

from django.db import models
from django.contrib.auth.models import AbstractUser
import re

class MyUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, primary_key=True)
    bio = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    POST_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('link', 'Link'),
    ]
    
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField(max_length=2000)
    post_type = models.CharField(max_length=10, choices=POST_TYPES, default='text')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    link_url = models.URLField(blank=True, null=True)
    link_image = models.URLField(blank=True, null=True)
    link_title = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(MyUser, related_name='post_likes', blank=True)

    def save(self, *args, **kwargs):
        # Auto-detect post type based on content
        if self.image:
            self.post_type = 'image'
        elif self.video_url and 'youtube.com' in self.video_url or 'youtu.be' in self.video_url:
            self.post_type = 'video'
        elif self.link_url:
            self.post_type = 'link'
        else:
            self.post_type = 'text'
        super().save(*args, **kwargs)

    def extract_youtube_id(self):
        """Extract YouTube video ID from URL"""
        if not self.video_url:
            return None
            
        # Handle different YouTube URL formats
        youtube_regex = (
            r'(https?://)?(www\.)?'
            r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
            r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        
        match = re.match(youtube_regex, self.video_url)
        if match:
            return match.group(6)
        return None

    def __str__(self):
        return f"Post by {self.user.username} - {self.post_type}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"