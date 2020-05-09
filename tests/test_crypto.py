from django.test import TestCase
from django.conf import settings
from mirage.crypto import Crypto


class TestCrypto(TestCase):

    def setUp(self):
        self.crypto = Crypto()
        self.value = 'hello,text'
        if getattr(settings, "MIRAGE_SECRET_KEY", None):
            self.encrypted = "4DIIbNsZPqO1DuXX1GjpkQ=="
        else:
            self.encrypted = 'pyy1FL2ftjBjUrJlGjgl3g=='

    def test_encrypt(self):
        self.assertEqual(self.crypto.encrypt(self.value), self.encrypted)

    def test_decrypt(self):
        self.assertEqual(self.crypto.decrypt(self.encrypted), self.value)
