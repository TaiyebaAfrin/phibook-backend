from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    get_user_profile_data, CustomTokenObtainPairView, CustomTokenRefreshView, 
    register, auhtenticated, toggleFollow, get_users_posts, toggleLike, 
    create_post, get_posts, search_users, logout, update_user_details,
    create_comment, get_comments, delete_comment, delete_post, initiate_payment, payment_cancel, payment_fail, payment_success,
)

urlpatterns = [
    path('user_data/<str:pk>/', get_user_profile_data),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register),
    path('authenticated/', auhtenticated),
    path('toggle_follow/', toggleFollow),
    path('posts/<str:pk>/', get_users_posts),
    path('toggleLike/', toggleLike),
    path('create_post/', create_post),
    path('get_posts/', get_posts),
    path('search/', search_users),
    path('update_user/', update_user_details),
    path('logout/', logout),
    
    # Comment routes
    path('create_comment/', create_comment),
    path('comments/<int:post_id>/', get_comments),
    path('delete_comment/<int:comment_id>/', delete_comment),
    
    # Delete routes
    path('delete_post/<int:post_id>/', delete_post),


    #payments
    path("payment/initiate/", initiate_payment, name="intiate-payment"),
    path("payment/success/", payment_success, name="payment-success"),
    path("payment/fail/", payment_fail, name="payment-fail"),
    path("payment/cancel/", payment_cancel, name="payment-cancel"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)