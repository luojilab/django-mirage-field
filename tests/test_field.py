from django.test import TestCase
from .models import TestModel


class TestField(TestCase):
    CHAR = 'hello,char'
    TEXT = 'hello,text'
    INTEGER = 1234567890
    EMAIL = 'hello@email.com'

    @classmethod
    def setUpTestData(cls):
        obj = TestModel.objects.create()
        obj.char = cls.CHAR
        obj.text = cls.TEXT
        obj.integer = cls.INTEGER
        obj.email = cls.EMAIL
        obj.save()

    def setUp(self):
        self.obj = TestModel.objects.latest('id')

    def test_char_field(self):
        self.assertEqual(self.obj.char, self.CHAR)
        self.assertEqual(type(self.obj.char), str)

    def test_text_field(self):
        self.assertEqual(self.obj.text, self.TEXT)
        self.assertEqual(type(self.obj.text), str)

    def test_int_field(self):
        self.assertEqual(self.obj.integer, self.INTEGER)
        self.assertEqual(type(self.obj.integer), int)

    def test_email_field(self):
        self.assertEqual(self.obj.email, self.EMAIL)
        self.assertEqual(type(self.obj.email), str)
