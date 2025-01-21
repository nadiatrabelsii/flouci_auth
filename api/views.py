from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate, login
from .models import Post
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

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
        
class CustomLoginView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) 
            return Response({
                "message": "Login successful",
                "username": username,
                "csrf_token": request.META.get("CSRF_COOKIE", None) 
            }, status=200)
        else:
            return Response({"message": "Invalid credentials"}, status=401)

class PostCreateView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response({"message": "Post created successfully"}, status=201)
        return Response(serializer.errors, status=400)
