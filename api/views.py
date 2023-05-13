from rest_framework import filters, generics, mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Follow, Group, Post
from .permissions import AuthorOrReadOnly, GroupOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().select_related('author')
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(PostViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        queryset = (
            Comment.objects.filter(
                post=post
            ).select_related('author')
        )
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            post=self.kwargs.get('post_id'),
            author=self.request.user
        )


class FollowViewSet(
    generics.ListCreateAPIView,generics.RetrieveDestroyAPIView,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
        else:
            user = None
        queryset = Follow.objects.filter(
            user=user
        ).prefetch_related('following')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (GroupOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
