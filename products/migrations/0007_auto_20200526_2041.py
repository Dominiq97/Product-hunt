# Generated by Django 2.0.2 on 2020-05-26 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='title',
            new_name='name',
        ),
    ]
