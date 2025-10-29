# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views



# from .views import get_user_profile_data, CustomTokenObtainPairView, CustomTokenRefreshView, register, auhtenticated, toggleFollow, get_users_posts, toggleLike, create_post, get_posts, search_users, logout, update_user_details, initiate_payment





# urlpatterns = [
#     path('user_data/<str:pk>/', get_user_profile_data),
#     path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
#     path('register/', register),
#     path('authenticated/', auhtenticated),
#     path('toggle_follow/', toggleFollow ),
#     path('posts/<str:pk>/', get_users_posts),
#     path('toggleLike/', toggleLike),
#     path('create_post/', create_post),
#     path('get_posts/', get_posts),
#     path('search/', search_users),
#     path('update_user/', update_user_details),
#     path('logout/', logout),
#     path("payment/initiate/", initiate_payment, name="intiate-payment"),






#     path('api/comments/create/', views.create_comment, name='create_comment'),
#     path('api/comments/<int:post_id>/', views.get_post_comments, name='get_post_comments'),
#     path('api/comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),



# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('authenticated/', views.auhtenticated),
    path('register/', views.register),
    path('token/', views.CustomTokenObtainPairView.as_view()),
    path('token/refresh/', views.CustomTokenRefreshView.as_view()),
    path('user_data/<str:pk>/', views.get_user_profile_data),
    path('toggle_follow/', views.toggleFollow),
    path('posts/<str:pk>/', views.get_users_posts),
    path('toggleLike/', views.toggleLike),
    path('create_post/', views.create_post),
    path('get_posts/', views.get_posts),
    path('search/', views.search_users),
    path('update_user/', views.update_user_details),
    path('logout/', views.logout),
    
    # Comment URLs
    path('api/comments/create/', views.create_comment),
    path('api/comments/<int:post_id>/', views.get_post_comments),
    path('api/comments/delete/<int:comment_id>/', views.delete_comment),
    
    # Payment URL
    path('initiate_payment/', views.initiate_payment),
]