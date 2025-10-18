from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from django.views.generic.base import RedirectView
from django.http import HttpResponse



from .views import get_user_profile_data, CustomTokenObtainPairView, CustomTokenRefreshView, register, auhtenticated, toggleFollow, get_users_posts, toggleLike, create_post, get_posts, search_users, logout, update_user_details
#intiate_payment



# Simple health check view
def health_check(request):
    return HttpResponse("Django app is running!")


urlpatterns = [
    path('user_data/<str:pk>/', get_user_profile_data),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register),
    path('authenticated/', auhtenticated),
    path('toggle_follow/', toggleFollow ),
    path('posts/<str:pk>/', get_users_posts),
    path('toggleLike/', toggleLike),
    path('create_post/', create_post),
    path('get_posts/', get_posts),
    path('search/', search_users),
    path('update_user/', update_user_details),
    path('logout/', logout),
    #path("payment/initiate/", intiate_payment, name="intiate-payment"),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path('favicon.png', RedirectView.as_view(url='/static/favicon.png', permanent=True)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)