# Generated by Django 3.0.5 on 2021-11-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmodel',
            name='textraw',
            field=models.TextField(blank=True, null=True),
        ),
    ]
