from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Prefetch
from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer
from rest_framework.views import APIView

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        # Optimize query by selecting related author and user
        queryset = Post.objects.select_related(
            'author',
            'author__user'
        ).filter(
            status='published'
        )
        
        # Add filtering options
        author_id = self.request.query_params.get('author_id')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
            
        return queryset

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer

    def get_queryset(self):
        # Optimize query by selecting related user and annotating posts count
        return Author.objects.select_related(
            'user'
        ).annotate(
            posts_count=Count('posts')
        ).prefetch_related(
            Prefetch(
                'posts',
                queryset=Post.objects.filter(status='published')
            )
        )

    @action(detail=True)
    def posts(self, request, pk=None):
        author = self.get_object()
        posts = Post.objects.filter(
            author=author,
            status='published'
        )
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class TestParamsView(APIView):
    def get(self, request):
        response_data = {
            "query_params": dict(request.query_params),
            "data": request.GET,
            "POST": dict(request.POST),
            "FILES": {
                key: {
                    "name": value.name,
                    "size": value.size,
                    "content_type": value.content_type
                } for key, value in request.FILES.items()
            },
            "method": request.method,
            "path": request.path,
            "path_info": request.path_info,
            "headers": dict(request.headers),
            "content_type": request.content_type,
            "content_params": request.content_params,
            "scheme": request.scheme,
            "server_name": request.META.get('SERVER_NAME'),
            "server_port": request.META.get('SERVER_PORT'),
            "cookies": request.COOKIES,
            "session": dict(request.session) if hasattr(request, 'session') else None,
            "user": str(request.user) if hasattr(request, 'user') else None,
            "auth": request.auth,
            "stream": request.stream
        }
        return Response(response_data)