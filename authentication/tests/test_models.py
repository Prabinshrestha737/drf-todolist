from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):


    def test_create_user(self):
        user = User.objects.create_user('prabin', 'test@prabin.com', 'passowr@1')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'test@prabin.com')
    

    def test_create_super_user(self):
        user = User.objects.create_superuser('prabin', 'test@prabin.com', 'passowr@1')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'test@prabin.com')
    

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email='test@prabin.com', passowrd='passowr@1')
        self.assertRaisesMessage(ValueError, 'The given user name must be set')

    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username="", email='test@prabin.com', passowrd='passowr@1')
    

    def test_cant_create_super_user_with_no_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username='username', email='ad@gmail.com', password='password123!@', is_staff=False)

    def test_cant_create_super_user_with_no_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username='username', email='ad@gmail.com', password='password123!@', is_superuser=False)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'ad', 'ad@gmail.com', 'password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'ad@gmail.com')