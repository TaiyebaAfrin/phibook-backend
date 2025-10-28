from rest_framework import serializers
from .models import MyUser, Post, Comment

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
    profile_image_url = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'profile_image', 'profile_image_url', 'follower_count', 'following_count']

    def get_follower_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count()
    
    def get_profile_image_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'text', 'formatted_date', 'like_count', 'user_has_liked']

    def get_username(self, obj):
        return obj.user.username
    
    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y")
    
    def get_user_has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(username=request.user.username).exists()
        return False

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    file_url = serializers.SerializerMethodField()
    file_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'username', 'description', 'image', 'file', 'image_url', 'file_url', 'file_name', 
                 'formatted_date', 'likes', 'like_count', 'comments', 'comment_count']

    def get_username(self, obj):
        return obj.user.username
    
    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y")
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_image_url(self, obj):
        if obj.image:
            # Cloudinary field returns the URL directly
            return obj.image.url
        return None
    
    def get_file_url(self, obj):
        if obj.file:
            # Cloudinary field returns the URL directly
            return obj.file.url
        return None
    
    def get_file_name(self, obj):
        if obj.file:
            # For Cloudinary, you might want to get the original filename
            return obj.file.name
        return None

class UserSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'email', 'profile_image', 'profile_image_url', 'first_name', 'last_name']

    def get_profile_image_url(self, obj):
        if obj.profile_image:
            return obj.profile_image.url
        return None