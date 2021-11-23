import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from django.conf import settings
from django.utils.encoding import force_bytes, force_str

SHORT_SECRET_KEY: str = """
django-mirage-field key length (MIRAGE_SECRET_KEY or SECRET_KEY) must be longer than 32 characters!
"""


class BaseCipher:
    def __init__(self, key, iv) -> None:
        self.key = key
        self.iv = iv

    def encrypt(self, text) -> str:
        return text

    def decrypt(self, encrypted) -> str:
        return encrypted


class ECBCipher(BaseCipher):

    def encrypt(self, text):
        encryptor = Cipher(algorithms.AES(self.key),
                           modes.ECB(), default_backend()).encryptor()
        padder = padding.PKCS7(algorithms.AES(self.key).block_size).padder()
        padded_data = padder.update(force_bytes(text)) + padder.finalize()
        encrypted_text = encryptor.update(padded_data) + encryptor.finalize()
        return force_str(base64.urlsafe_b64encode(encrypted_text))

    def decrypt(self, encrypted):
        decryptor = Cipher(algorithms.AES(self.key),
                           modes.ECB(), default_backend()).decryptor()
        padder = padding.PKCS7(algorithms.AES(self.key).block_size).unpadder()
        decrypted_text = decryptor.update(base64.urlsafe_b64decode(encrypted))
        unpadded_text = padder.update(decrypted_text) + padder.finalize()
        return force_str(unpadded_text)


class CBCCipher(BaseCipher):

    def encrypt(self, text) -> str:
        encryptor = Cipher(algorithms.AES(self.key), modes.CBC(
            self.iv), default_backend()).encryptor()
        padder = padding.PKCS7(algorithms.AES(self.key).block_size).padder()
        padded_data = padder.update(force_bytes(text)) + padder.finalize()
        encrypted_text = encryptor.update(padded_data) + encryptor.finalize()
        return force_str(base64.urlsafe_b64encode(encrypted_text))

    def decrypt(self, encrypted) -> str:
        decryptor = Cipher(algorithms.AES(self.key), modes.CBC(
            self.iv), default_backend()).decryptor()
        padder = padding.PKCS7(algorithms.AES(self.key).block_size).unpadder()
        decrypted_text = decryptor.update(base64.urlsafe_b64decode(encrypted))
        unpadded_text = padder.update(decrypted_text) + padder.finalize()
        return force_str(unpadded_text)


class Crypto:

    def __init__(self, key=None, mode=None, iv=None):
        if not key:
            key = getattr(settings, "MIRAGE_SECRET_KEY",
                          None) or getattr(settings, "SECRET_KEY")
        assert len(key) >= 32, SHORT_SECRET_KEY
        key = base64.urlsafe_b64encode(force_bytes(key))[:32]
        if mode is None:
            mode = getattr(settings, "MIRAGE_CIPHER_MODE", "ECB")
        if iv is None:
            iv = getattr(settings, "MIRAGE_CIPHER_IV", "1234567890abcdef")
        self.cipher = eval(f"{mode}Cipher")(key=key, iv=force_bytes(iv))

    def encrypt(self, text):
        if text is None:
            return None
        try:
            self.cipher.decrypt(text)
            return text
        except Exception:
            return self.cipher.encrypt(text)

    def decrypt(self, encrypted):
        if encrypted is None:
            return None
        try:
            return self.cipher.decrypt(encrypted)
        except Exception:
            return encrypted
