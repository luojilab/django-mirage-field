from django.db import models
from mirage import fields


class TestModel(models.Model):
    char = fields.EncryptedCharField(blank=True, null=True)
    text = fields.EncryptedTextField(blank=True, null=True)
    integer = fields.EncryptedIntegerField(blank=True, null=True)
    email = fields.EncryptedEmailField(blank=True, null=True)
