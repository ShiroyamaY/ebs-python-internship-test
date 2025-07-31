from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category
from apps.blog.serializers import BlogSerializer, CategorySerializer, CommentSerializer
from apps.common.permissions import ReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListCreateView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get_permissions(self):
        if self.request.method == "GET":
            return [ReadOnly()]
        return [IsAuthenticated()]

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        blog: Blog = Blog.objects.create(**validated_data)

        return Response(self.serializer_class(blog).data, status=status.HTTP_201_CREATED)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)

        return Response(self.get_serializer(blog).data)


class BlogCommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def get_blog(self):
        return get_object_or_404(Blog, id=self.kwargs["blog_id"])

    def perform_create(self, serializer):
        blog: Blog = self.get_blog()
        serializer.save(blog=blog)
