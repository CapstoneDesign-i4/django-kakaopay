# Generated by Django 4.0.3 on 2022-04-29 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchat', '0026_product_modify_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='modify_date',
        ),
    ]