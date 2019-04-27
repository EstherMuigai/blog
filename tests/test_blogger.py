from app.models import Blogger
import unittest
from app import db

class BloggerTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blogger Model
    '''

def setUp(self):
        self.blogger_Beautiful = Blogger(firstname = 'Beautiful',lastname = 'Creature',username = 'Beau',
        pass_secure = 'what',bio = 'Only beautiful things',email = 'bcreature@heaven.com',
        profile_pic_path = '/heavens/gate')

def test_check_instance_variables(self):
        self.assertEquals(self.blogger_Beautiful.firstname,'Beautiful')
        self.assertEquals(self.blogger_Beautiful.lastname,'Creature')
        self.assertEquals(self.blogger_Beautiful.username,'Beau')
        self.assertEquals(self.blogger_Beautiful.pass_secure,'what')
        self.assertEquals(self.blogger_Beautiful.bio,'Only beautiful things')
        self.assertEquals(self.blogger_Beautiful.email,'bcreature@heaven.com')
        self.assertEquals(self.blogger_Beautiful.profile_pic_path,'/heavens/gate')

def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

def test_no_access_password(self):
        with self.assertRaises(AttributeError):
                self.new_user.password

def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('what'))

def tearDown(self):
        Blogger.query.delete()
