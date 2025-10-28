from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('user_data/<str:pk>/', views.get_user_profile_data),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.register),
    path('authenticated/', views.auhtenticated),
    path('toggle_follow/', views.toggleFollow),
    path('posts/<str:pk>/', views.get_users_posts),
    path('toggleLike/', views.toggleLike),
    path('create_post/', views.create_post),
    path('delete_post/<int:pk>/', views.delete_post),
    path('get_posts/', views.get_posts),
    path('search/', views.search_users),
    path('update_user/', views.update_user_details),
    path('logout/', views.logout),
    
    # Comment endpoints
    path('create_comment/', views.create_comment),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('toggle_comment_like/', views.toggle_comment_like),
    path('post_comments/<int:pk>/', views.get_post_comments),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  