# Generated by Django 4.0.3 on 2022-04-29 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchat', '0024_remove_product_modify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='lock_num',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reservation',
        ),
    ]