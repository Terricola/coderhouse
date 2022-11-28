import random
import string
from django.contrib.auth.models import User
from django.test import TestCase
from post.models import Post

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
            username="testuser",
            password="12345678",
        )
        Post.objects.create(title="¿Pregunta generica 1?", tag="debate", owner=self.test_user)
        Post.objects.create(title="Pregunta generica 2", tag="tecnologia", owner=self.test_user)

        post_test_num = 20
        self.mock_titles = [
            "".join(
                [
                    random.choice((string.ascii_letters + string.digits))
                    for _ in range(random.randint(4, 20))
                ]
            )
            for _ in range(post_test_num)
        ]
        self.mock_tags = [
            int(
                "".join(
                    [
                        random.choice((string.digits))
                        for _ in range(random.randint(3, 9))
                    ]
                )
            )
            for _ in range(post_test_num)
        ]

        for mock_title, mock_tag in zip(self.mock_titles, self.mock_tags):
            Post.objects.create(title=mock_title, tag=mock_tag, owner=self.test_user)

    def test_post_model(self):
        """Post creation are correctly identified"""
        generica1_post = Post.objects.get(title="¿Pregunta generica 1?")
        generica2_post = Post.objects.get(title="Pregunta generica 2")
        self.assertEqual(generica1_post.owner.username, "testuser")
        self.assertEqual(generica2_post.owner.username, "testuser")
        self.assertEqual(generica1_post.tag, "debate")
        self.assertEqual(generica2_post.tag, "tecnologia")

    def test_post_list(self):
        for mock_title, mock_tag in zip(self.mock_titles, self.mock_tags):
            post_test = Post.objects.get(title=mock_title)
            self.assertEqual(post_test.owner.username, "testuser")
            self.assertEqual(post_test.tag, mock_tag)