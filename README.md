# django-mirage-field

![](https://img.shields.io/pypi/v/django-mirage-field.svg?label=django-mirage-field)

## Introduce

A Django model field that encrypt your data when save to and decrypt when get from database. It keeps data always encrypted in database.

## Support

* Use settings.SECRET_KEY as secret key default or anyelse
* Support CharField、TextField、IntegerField、EmailField
* Support Django ORM's `get()`、`filter()` query method
* Use AES-256-ECB algorithm
* Support PostgreSQL and MySQL database

## Example
```
from mirage import fields
class TestModel(models.Model):
    phone = fields.EncryptedCharField()
```

```
obj = TestModel.objects.get(phone=18866677777)
obj.id    # 123
obj.phone # "18866677777"
```
```psql
yourdatabase=# select * from testmodel where id = 123;
         id          |           name
---------------------+--------------------------
 123 | -bYijegsEDrmS1s7ilnspA==
```

## Installation

```bash
pip install django-mirage-field
```

## Settings

1. Add`mirage`to`INSTALLED_APPS`

1. import

```
from mirage import fields
class TestModel(models.Model):
    phone = fields.EncryptedCharField()
```

## Model Fields

* EncryptedTextField
* EncryptedCharField
* EncryptedEmailField
* EncryptedIntegerField

## Data Migrate

### via migrations

add `app_name`,`model_name`,`app_name` in [migrations.RunPython](https://docs.djangoproject.com/en/2.2/ref/migration-operations/#runpython)

```
from mirage.tools import Migrator

migrations.RunPython(Migrator("app_name", "model_name", "field_name").encrypt, reverse_code=Migrator("app_name", 'model_name', 'field_name').decrypt),
```

### Management command

Options:

* --app
* --model
* --field
* --method (optional: `encrypt`, `decrypt`, `encrypt_to`, `decrypt_to`, `copy`)
* --tofield (need when use `encryt_to`, `decrypt_to`, `copy` method)

Optional options:

* --offset ("select * from xxx where id > offset")
* --total ("select * from xxx order by id limit total")

Examples

```
./manage.py mirage --app=yourapp --model=testmodel --field=address --method=encrypt --offset=2000000 --total=3000000

./manage.py mirage --app=yourapp --model=testmodel --field=address --method=encrypt_to --tofield=encrypted_address

```

## Exceptions

```
from mirage import exceptions
```

### EncryptedFieldException

## Algorithm

*  AES-256-ECB

## Performance

Migrate data: 6000,000 columns takes 40 minutes, Average 1 column/2.5ms

Only encrypt/decrypt: Average 1 value/ms

## Clients

* [Java](https://github.com/luojilab/django-mirage-field/tree/master/client/java)