# Generated by Django 3.1.3 on 2022-02-27 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchat', '0017_auto_20220223_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='key',
        ),
    ]
