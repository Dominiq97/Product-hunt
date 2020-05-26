# Generated by Django 2.0.2 on 2020-05-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('syntax', models.CharField(max_length=255)),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]