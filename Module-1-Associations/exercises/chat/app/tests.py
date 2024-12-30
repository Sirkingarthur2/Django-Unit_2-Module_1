from django.test import TestCase
from app.models import *

class ChatAppTests(TestCase):
    def test_create_channel(self):
        create_channel("General")
        result = Channel.objects.get(name = "General")
        self.assertEqual(result.name, "General")
        self.assertEqual(result.users.count(), 0)

    def test_create_user(self):
        user1 = create_user("Alice")
        self.assertEqual(user1.name, "Alice")

    def test_create_message(self):
        user1 = create_user("Alice")
        channel = create_channel("General")
        create_message(user1, channel, "Hello, World!")
        messages = messages_for(channel)
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].text, "Hello, World!")

    def test_messages_for(self):
        user1 = create_user("Alice")
        user2 = create_user("Bob")
        channel = create_channel("General")
        create_message(user1, channel, "Hello, World!")
        create_message(user2, channel, "Hi there!")

        messages = messages_for(channel)
        self.assertEqual(len(messages), 2)
        self.assertEqual(messages[0].text, "Hello, World!")
        self.assertEqual(messages[1].text, "Hi there!")

    def test_active_users(self):
        # Create users
        user1 = User.objects.create(name='Alice')
        user2 = User.objects.create(name='Bob')
        user3 = User.objects.create(name='Charlie')

        # Create a channel
        channel = Channel.objects.create(name='General')

        # Create messages
        Message.objects.create(user=user1, channel=channel, text='Hello!')
        Message.objects.create(user=user2, channel=channel, text='Hi there!')

        # Get active users
        active = active_users(channel)

        # Assert that the active users are correct
        self.assertIn(user1, active)
        self.assertIn(user2, active)
        self.assertNotIn(user3, active)
        self.assertEqual(active.count(), 2)

    def test_lurkers(self):
        # Create users
        user1 = User.objects.create(name='Alice')
        user2 = User.objects.create(name='Bob')
        user3 = User.objects.create(name='Charlie')

        # Create a channel
        channel = Channel.objects.create(name='General')

        # Create messages
        Message.objects.create(user=user1, channel=channel, text='Hello!')

        # Get lurkers
        lurkers_list = lurkers(channel)

        # Assert that the lurkers are correct
        self.assertIn(user2, lurkers_list)
        self.assertIn(user3, lurkers_list)
        self.assertNotIn(user1, lurkers_list)
        self.assertEqual(lurkers_list.count(), 2) 