import json
from django.test import TestCase
from apps.models import TestModel


class TestField(TestCase):
    CHAR = 'hello,char'
    TEXT = 'hello,text'
    INTEGER = 1234567890
    EMAIL = 'hello@email.com'
    URL = 'https://yindongliang.com'
    JSON = {"hello": "world", "foo": "bar"}

    @classmethod
    def setUpTestData(cls):
        obj = TestModel.objects.create()
        obj.char = cls.CHAR
        obj.text = cls.TEXT
        obj.integer = cls.INTEGER
        obj.email = cls.EMAIL
        obj.url = cls.URL
        obj.json = cls.JSON
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

    def test_url_field(self):
        self.assertEqual(self.obj.url, self.URL)
        self.assertEqual(type(self.obj.url), str)

    def test_json_field(self):
        self.assertEqual(self.obj.json, self.JSON)
        self.assertEqual(type(self.obj.json), dict)
