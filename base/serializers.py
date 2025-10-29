# from rest_framework import serializers
# from .models import MyUser, Post, Comment

# class UserRegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = MyUser
#         fields = ['username', 'email', 'first_name', 'last_name', 'password']

#     def create(self, validated_data):
#         user = MyUser(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user

# class MyUserProfileSerializer(serializers.ModelSerializer):
#     follower_count = serializers.SerializerMethodField()
#     following_count = serializers.SerializerMethodField()

#     class Meta:
#         model = MyUser
#         fields = ['username', 'bio', 'profile_image', 'follower_count', 'following_count']

#     def get_follower_count(self, obj):
#         return obj.followers.count()
    
#     def get_following_count(self, obj):
#         return obj.following.count()

# class CommentSerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField()
#     profile_image = serializers.SerializerMethodField()
#     formatted_date = serializers.SerializerMethodField()

#     class Meta:
#         model = Comment
#         fields = ['id', 'username', 'profile_image', 'text', 'formatted_date', 'user']

#     def get_username(self, obj):
#         return obj.user.username

#     def get_profile_image(self, obj):
#         if obj.user.profile_image:
#             return obj.user.profile_image.url
#         return None

#     def get_formatted_date(self, obj):
#         return obj.created_at.strftime("%d %b %y")


# class PostSerializer(serializers.ModelSerializer):
#     username = serializers.SerializerMethodField()
#     like_count = serializers.SerializerMethodField()
#     formatted_date = serializers.SerializerMethodField()
#     comment_count = serializers.SerializerMethodField()
#     comments = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Post
#         fields = ['id', 'username', 'description', 'formatted_date', 'likes', 'like_count', 'comment_count', 'comments']

#     def get_username(self, obj):
#         return obj.user.username
    
#     def get_like_count(self, obj):
#         return obj.likes.count()
    
#     def get_formatted_date(self, obj):
#         return obj.created_at.strftime("%d %b %y")
    
#     def get_comment_count(self, obj):
#         return obj.comments.count()
        
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ['username', 'bio', 'email', 'profile_image', 'first_name', 'last_name']

# class CreateCommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['text']


from rest_framework import serializers
from .models import MyUser, Post, Comment
import re

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = MyUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MyUserProfileSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'profile_image', 'follower_count', 'following_count']

    def get_follower_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count()

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'profile_image', 'text', 'formatted_date', 'user']

    def get_username(self, obj):
        return obj.user.username

    def get_profile_image(self, obj):
        if obj.user.profile_image:
            return obj.user.profile_image.url
        return None

    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y")

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    youtube_id = serializers.SerializerMethodField()
    user_profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'username', 'user_profile_image', 'description', 'formatted_date', 
            'likes', 'like_count', 'comment_count', 'comments', 'post_type',
            'image', 'video_url', 'link_url', 'link_image', 'link_title', 'youtube_id'
        ]

    def get_username(self, obj):
        return obj.user.username
    
    def get_user_profile_image(self, obj):
        if obj.user.profile_image:
            return obj.user.profile_image.url
        return None
    
    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y")
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_youtube_id(self, obj):
        return obj.extract_youtube_id()
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'email', 'profile_image', 'first_name', 'last_name']

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['description', 'image', 'video_url', 'link_url']