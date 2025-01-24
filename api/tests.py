from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword123"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpassword123"))


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testauthor",
            password="testpassword123"
        )
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author, self.user)

    def test_post_str_representation(self):
        self.assertEqual(str(self.post), "Test Post")


class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="serializeruser",
            password="serializerpassword"
        )
        self.post = Post.objects.create(
            title="Serialized Post",
            content="This post is for testing the serializer.",
            author=self.user
        )
        self.serializer = PostSerializer(instance=self.post)

    def test_serializer_fields(self):
        data = self.serializer.data
        self.assertEqual(data["title"], "Serialized Post")
        self.assertEqual(data["content"], "This post is for testing the serializer.")
        self.assertEqual(data["author"], "serializeruser")

class ViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="nadia",
            password="joujoujou123"
        )

        self.client = APIClient()

        self.token_url = "/api/token/"
        self.login_url = "/login/"
        self.posts_url = "/api/posts/"
        self.create_post_url = "/api/posts/create/"
        self.post_detail_url = "/api/posts/1/"

        self.api_key = "YX3q1mR9.5u0YyZzUvwFCKy95vew605rlrEeqAHz3"

        self.post = Post.objects.create(
            title="My New Post",
            content="This is the content of my new post.",
            author=self.user
        )

    def test_post_list_with_jwt(self):
        response = self.client.post(
            self.token_url, 
            {"username": "nadia", "password": "joujoujou123"}
        )
        self.assertEqual(response.status_code, 200)
        tokens = response.json()
        access_token = tokens.get("access")
        self.assertIsNotNone(access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
        response = self.client.get(self.posts_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        print(f"Post List Response: {response.json()}")

    def test_post_detail_with_api_key(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Api-Key {self.api_key}")
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        post_data = response.json()
        self.assertEqual(post_data["title"], "My New Post")
        self.assertEqual(post_data["content"], "This is the content of my new post.")
        print(f"Post Detail Response: {post_data}")

    def test_custom_login_view(self):
        response = self.client.post(
            self.login_url,
            {"username": "nadia", "password": "joujoujou123"}
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Login successful")
        self.assertEqual(data["username"], "nadia")
        self.assertIsNotNone(data.get("csrf_token"))
        print(f"Login Response: {data}")

        response = self.client.post(
            self.login_url,
            {"username": "nadia", "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json()["message"], "Invalid credentials")

    def test_post_create_with_session(self):
        login_response = self.client.post(
            self.login_url,
            {"username": "nadia", "password": "joujoujou123"}
        )
        self.assertEqual(login_response.status_code, 200)
        csrf_token = login_response.cookies.get("csrftoken").value
        session_id = login_response.cookies.get("sessionid").value
        self.assertIsNotNone(csrf_token)
        self.assertIsNotNone(session_id)

        self.client.cookies["csrftoken"] = csrf_token
        self.client.cookies["sessionid"] = session_id

        create_post_data = {
            "title": "Another Test Post",
            "content": "This is another test post.",
            "author": '1'
        }
        response = self.client.post(
            self.create_post_url,
            data=create_post_data,
            HTTP_X_CSRFTOKEN=csrf_token
        )
        self.assertEqual(response.status_code, 201)
        print(f"Post Create Response: {response.json()}")

        response = self.client.get(self.posts_url)
        self.assertEqual(len(response.json()), 2) 
