from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogCommentCreateView, BlogItemView, BlogListCreateView, CategoryViewSet

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListCreateView.as_view(), name="blog"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/<int:blog_id>/comments", BlogCommentCreateView.as_view(), name="comment"),
    *router.urls,
]
