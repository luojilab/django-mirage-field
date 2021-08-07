# django-mirage-field

![](https://img.shields.io/pypi/v/django-mirage-field.svg?label=django-mirage-field)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fluojilab%2Fdjango-mirage-field&count_bg=%233DC8BC&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=views&edge_flat=false)](https://hits.seeyoufarm.com)

## Introduce

A Django model field that encrypt your data when save to DB and decrypt when get from DB. It keeps data always encrypted in DB. Base on AES, it supports query method like `get()` and `filter()` in Django.

Mirage can also migrate data from origin column to encrypted column in database with a good performance.

## Features

* Use settings.SECRET_KEY as secret key default or anyelse which length >= 32
* Support CharField、TextField、IntegerField、EmailField
* Support Django ORM's `get()`、`filter()` query method
* Support AES-256-ECB and AES-256-CBC(v1.2.0)
* Support PostgreSQL and MySQL database
* Support Django model field `db_index` and `unique` attributes

## Installation

```bash
pip install django-mirage-field
```

## Usage

```python
from mirage import fields
class TestModel(models.Model):
    age = fields.EncryptedIntegerField()
```

```python
obj = TestModel.objects.get(age=18)
obj.id          # 1
obj.age         # 18
type(obj.age)   # int
```

```psql
database=# select * from testmodel where id = 1;
         id          |           age
---------------------+--------------------------
 1 | -bYijegsEDrmS1s7ilnspA==
```

```python
from mirage.crypto import Crypto
c = Crypto(key="")                      # key is optional, default will use settings.SECRET_KEY
c.encrypt('some_address')               # -bYijegsEDrmS1s7ilnspA==
c.decrypt('-bYijegsEDrmS1s7ilnspA==')   # some_address
```

## Settings

- MIRAGE_SECRET_KEY
- MIRAGE_CIPHER_MODE (v1.2)
- MIRAGE_CIPHER_IV (v1.2)

### MIRAGE_SECRET_KEY

You can use the `settings.SECRET_KEY` as default key, if you want custom another key for mirage, set the `MIRAGE_SECRET_KEY` in settings.

Mirage will get the `settings.MIRAGE_SECRET_KEY` first, if not set, mirage will get the `settings.SECRET_KEY`.

### MIRAGE_CIPHER_MODE

`MIRAGE_CIPHER_MODE` is optional, choices are below, If don't set, default is `ECB`.

- `ECB`
- `CBC`

### MIRAGE_CIPHER_IV

`MIRAGE_CIPHER_IV` is optional, if you don't set, it will use a default: "1234567890abcdef", it's length must be 16.


## Model Fields

1. EncryptedTextField
2. EncryptedCharField
3. EncryptedEmailField
4. EncryptedIntegerField

## Data Migrate

Add`mirage`to`INSTALLED_APPS`

### 1. Migrations

add `app_name`,`model_name`,`field_name` in [migrations.RunPython](https://docs.djangoproject.com/en/2.2/ref/migration-operations/#runpython)

```
from mirage.tools import Migrator

migrations.RunPython(Migrator("app_name", "model_name", "field_name").encrypt, reverse_code=Migrator("app_name", 'model_name', 'field_name').decrypt),
```

### 2. Commands

Options:

* --app
* --model
* --field
* --method (optional: `encrypt`, `decrypt`, `encrypt_to`, `decrypt_to`, `copy_to`)
* --tofield (need when use `encryt_to`, `decrypt_to`, `copy_to` method)

Optional options:

* --offset ("select * from xxx where id > offset")
* --total ("select * from xxx order by id limit total")
* --limit: set the query count in every update, default is 1000, if you set -1, mirage will query all rows one time to update.

Examples

```
./manage.py mirage --app=yourapp --model=testmodel --field=address --method=encrypt --offset=2000000 --total=3000000

./manage.py mirage --app=yourapp --model=testmodel --field=address --method=encrypt_to --tofield=encrypted_address

```

## Exceptions

```
from mirage import exceptions
```

1. EncryptedFieldException

## Performance

### With ECB mode

Migrate data: 6000,000 columns takes 40 minutes, Average 1 column/2.5ms

Only encrypt/decrypt: Average 1 value/ms

## Clients

* [Java](https://github.com/luojilab/django-mirage-field/tree/master/client/java)