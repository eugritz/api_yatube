from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .viewsets import GroupViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
