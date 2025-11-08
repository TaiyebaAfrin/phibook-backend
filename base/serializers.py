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
#     username = serializers.CharField(source='user.username', read_only=True)
#     formatted_date = serializers.SerializerMethodField()
#     can_delete = serializers.SerializerMethodField()

#     class Meta:
#         model = Comment
#         fields = ['id', 'username', 'text', 'formatted_date', 'user', 'can_delete']

#     def get_formatted_date(self, obj):
#         return obj.created_at.strftime("%d %b %y %H:%M")
    
#     def get_can_delete(self, obj):
#         request = self.context.get('request')
#         if request and request.user.is_authenticated:
#             return obj.user.username == request.user.username or obj.post.user.username == request.user.username
#         return False

# class PostSerializer(serializers.ModelSerializer):
#     username = serializers.CharField(source='user.username', read_only=True)
#     like_count = serializers.SerializerMethodField()
#     formatted_date = serializers.SerializerMethodField()
#     comment_count = serializers.SerializerMethodField()
#     can_delete = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = ['id', 'username', 'description', 'formatted_date', 'likes', 'like_count', 'comment_count', 'can_delete']

#     def get_like_count(self, obj):
#         return obj.likes.count()
    
#     def get_formatted_date(self, obj):
#         return obj.created_at.strftime("%d %b %y")
    
#     def get_comment_count(self, obj):
#         return obj.comments.count()
    
#     def get_can_delete(self, obj):
#         request = self.context.get('request')
#         if request and request.user.is_authenticated:
#             return obj.user.username == request.user.username
#         return False

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = ['username', 'bio', 'email', 'profile_image', 'first_name', 'last_name']



from rest_framework import serializers
from .models import MyUser, Post, Comment

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'subscription_plan']  # Add subscription_plan

    def create(self, validated_data):
        user = MyUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            subscription_plan=validated_data.get('subscription_plan', 'free')  # Add this line
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MyUserProfileSerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'profile_image', 'follower_count', 'following_count', 'subscription_plan']  # Add subscription_plan

    def get_follower_count(self, obj):
        return obj.followers.count()
    
    def get_following_count(self, obj):
        return obj.following.count()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'bio', 'email', 'profile_image', 'first_name', 'last_name', 'subscription_plan']  # Add subscription_plan

# Your other serializers (CommentSerializer, PostSerializer) remain the same
class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    formatted_date = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'username', 'text', 'formatted_date', 'user', 'can_delete']

    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y %H:%M")
    
    def get_can_delete(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.user.username == request.user.username or obj.post.user.username == request.user.username
        return False

class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    like_count = serializers.SerializerMethodField()
    formatted_date = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    can_delete = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'username', 'description', 'formatted_date', 'likes', 'like_count', 'comment_count', 'can_delete']

    def get_like_count(self, obj):
        return obj.likes.count()
    
    def get_formatted_date(self, obj):
        return obj.created_at.strftime("%d %b %y")
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_can_delete(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.user.username == request.user.username
        return False