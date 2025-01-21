from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_api_key.permissions import HasAPIKey
from .models import Post
from .serializers import PostSerializer

class PostListView(APIView):
    permission_classes = [IsAuthenticated] 

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostDetailView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=200)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)
