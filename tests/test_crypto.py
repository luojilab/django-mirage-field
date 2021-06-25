from django.test import TestCase
from mirage.crypto import Crypto


class TestCryptoECB(TestCase):

    def setUp(self):
        self.crypto = Crypto(mode='ECB')
        self.value = 'hello,text'
        self.encrypted = "4DIIbNsZPqO1DuXX1GjpkQ=="

    def test_ecb_encrypt(self):
        self.assertEqual(self.crypto.encrypt(self.value), self.encrypted)

    def test_ecb_decrypt(self):
        self.assertEqual(self.crypto.decrypt(self.encrypted), self.value)


class TestCryptoCBC(TestCase):

    def setUp(self) -> None:
        self.crypto = Crypto(mode='CBC')
        self.value = 'hello,text'
        self.encrypted = "E_RFOSafjW-FQ-PDkXkv5g=="

    def test_cbc_encrypt(self):
        self.assertEqual(self.crypto.encrypt(self.value), self.encrypted)

    def test_cbc_decrypt(self):
        self.assertEqual(self.crypto.decrypt(self.encrypted), self.value)
