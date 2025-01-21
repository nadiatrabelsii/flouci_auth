from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from .models import User, Post, UserAPIKey


class APIAuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.post = Post.objects.create(title="Test Post", content="Test Content", author=self.user)
        self.api_key, self.key = UserAPIKey.objects.create_key(name="Test Key", user=self.user)

    def test_post_list_with_valid_jwt(self):
        token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_with_valid_api_key(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {self.key}")
        response = self.client.get(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 200)
