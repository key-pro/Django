from django.test import TestCase, Client
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Group, Message

# Create your tests here.

"""class SnsTests(TestCase):
    
    def test_check(self):
        x = True
        self.assertTrue(x)
        y = 100
        self.assertGreater(y, 0)
        arr = [10, 20, 30]
        self.assertIn(20, arr)
        nn = None
        self.assertIsNone(nn)
"""



"""class SnsTests(TestCase):
    def test_check(self):
        usr = User.objects.first()
        self.assertIsNotNone(usr)
        msg = Message.objects.first()
        self.assertIsNotNone(msg)
"""

"""class SnsTests(TestCase):
        
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        (usr, grp) = cls.create_user_and_group()
        cls.create_message(usr, grp)

    @classmethod
    def create_user_and_group(cls):
        # Create public user & public group.
        User(username="root", password="rootroot", is_staff=False, is_active=True).save()
        pb_usr = User.objects.filter(username='root').first()
        Group(title='root', owner_id=pb_usr.id).save()
        pb_grp = Group.objects.filter(title='root').first()

        # Create test user
        User(username="User", password="UserUserUser", is_staff=True, is_active=True).save()
        usr = User.objects.filter(username='User').first()

        return (usr, pb_grp)

    @classmethod
    def create_message(cls, usr, grp):
        # Create test message
        Message(content='this is test message.', owner_id=usr.id, group_id=grp.id).save()
        Message(content='test', owner_id=usr.id, group_id=grp.id).save()
        Message(content="ok", owner_id=usr.id, group_id=grp.id).save()
        Message(content="ng", owner_id=usr.id, group_id=grp.id).save()
        Message(content='finish', owner_id=usr.id, group_id=grp.id).save()

    def test_check(self):
        usr = User.objects.first()
        self.assertIsNotNone(usr)
        msg = Message.objects.first()
        self.assertIsNotNone(msg)
    

def test_check(self):
    usr = User.objects.filter(username='test').first()

    msg = Message.objects.filter(content="test").first()
    self.assertIs(msg.owner_id, usr.id)
    self.assertEqual(msg.owner.username, usr.username)
    self.assertEqual(msg.group.title, 'public')

    msgs = Message.objects.filter(content__contains="test").all()
    self.assertIs(msgs.count(), 2)
    
    c = Message.objects.all().count()
    self.assertIs(c,5)
    
    msg1 = Message.objects.all().first()
    msg2 = Message.objects.all().last()
    self.assertIsNot(msg1, msg2)
"""

class SnsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        (usr, grp) = cls.create_user_and_group()
        cls.create_message(usr, grp)

    @classmethod
    def create_user_and_group(cls):
        # Create public user & public group.
        User(username="root", password="rootroot", is_staff=False, is_active=True).save()
        pb_usr = User.objects.filter(username='root').first()
        Group(title='root', owner_id=pb_usr.id).save()
        pb_grp = Group.objects.filter(title='root').first()

        # Create test user
        User(username="User", password="UserUser", is_staff=True, is_active=True).save()
        usr = User.objects.filter(username='User').first()

        return (usr, pb_grp)

    @classmethod
    def create_message(cls, usr, grp):
        # Create test message
        Message(content='this is test message.', owner_id=usr.id, group_id=grp.id).save()
        Message(content='test', owner_id=usr.id, group_id=grp.id).save()
        Message(content="ok", owner_id=usr.id, group_id=grp.id).save()
        Message(content="ng", owner_id=usr.id, group_id=grp.id).save()
        Message(content='finish', owner_id=usr.id, group_id=grp.id).save()

    def test_check(self):
        usr = User.objects.filter(username='test').first()

        # access to SNS.
        response = self.client.get(reverse('index'))
        self.assertIs(response.status_code, 302)

        # login test account and access to SNS.
        self.client.force_login(usr)
        response = self.client.get(reverse('index'))
        self.assertIs(response.status_code, 200)
        self.assertContains(response, 'this is test message.')