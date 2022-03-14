import json
from django.core import exceptions
from django.db import models
from .crypto import Crypto
from .exceptions import EncryptedFieldException
from django.db.models.fields.json import KeyTransform


class EncryptedMixin(models.Field):
    internal_type = "CharField"
    prepared_max_length = None

    def __init__(self, key=None, **kwargs):
        kwargs.setdefault('max_length', self.prepared_max_length)
        self.crypto = Crypto(key)
        super().__init__(**kwargs)

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)
        if value is not None:
            encrypted_text = self.crypto.encrypt(value)
            if self.max_length and len(encrypted_text) > self.max_length:
                raise EncryptedFieldException(
                    f"Field {self.name} max_length={self.max_length} encrypted_len={len(encrypted_text)}"
                )
            return encrypted_text
        return None

    def from_db_value(self, value, expression, connection, *args):
        if value is None:
            return value
        return self.to_python(self.crypto.decrypt(value))

    def get_internal_type(self):
        return self.internal_type


class EncryptedTextField(EncryptedMixin, models.TextField):
    internal_type = "TextField"

class EncryptedJSONField(EncryptedMixin, models.JSONField):
    internal_type = "TextField"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        if isinstance(expression, KeyTransform) and not isinstance(value, str):
            return value
        try:
            return json.loads(self.crypto.decrypt(value), cls=self.decoder)
        except json.JSONDecodeError as e:
            return self.crypto.decrypt(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return json.dumps(self.crypto.encrypt(json.dumps(value, cls=self.encoder)), cls=self.encoder)


class EncryptedCharField(EncryptedMixin, models.CharField):
    prepared_max_length = 255


class EncryptedURLField(EncryptedMixin, models.URLField):
    prepared_max_length = 200


class EncryptedEmailField(EncryptedMixin, models.EmailField):
    prepared_max_length = 254


class EncryptedIntegerField(EncryptedMixin, models.CharField):
    prepared_max_length = 64

    def to_python(self, value):
        try:
            return int(value)
        except (TypeError, ValueError):
            return value

    def check(self, **kwargs):
        return [
            *super(models.CharField, self).check(**kwargs),
        ]
