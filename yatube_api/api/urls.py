from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import path, include

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    r'groups',
    GroupViewSet,
    basename='groups'
)
v1_router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls)),
]
