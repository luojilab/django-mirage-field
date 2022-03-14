from email.policy import default
from django.db import models
from mirage import fields


class TestModel(models.Model):
    char = fields.EncryptedCharField(blank=True, null=True)
    text = fields.EncryptedTextField(blank=True, null=True)
    textraw = models.TextField(blank=True, null=True)
    integer = fields.EncryptedIntegerField(blank=True, null=True)
    email = fields.EncryptedEmailField(blank=True, null=True)
    url = fields.EncryptedURLField(blank=True, null=True)
    json = fields.EncryptedJSONField(default={})
