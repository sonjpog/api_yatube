from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'

v1_router = routers.DefaultRouter()
v1_router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet,
    basename='comment'
)
v1_router.register(
    'groups',
    GroupViewSet,
    basename='group'
)
v1_router.register(
    'posts',
    PostViewSet,
    basename='post'
)

v1_api_patterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(v1_router.urls)),
]

urlpatterns = [
    path('v1/', include(v1_api_patterns)),
]
