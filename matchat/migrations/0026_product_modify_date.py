# Generated by Django 4.0.3 on 2022-04-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchat', '0025_remove_product_lock_num_remove_product_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modify_date',
            field=models.DateTimeField(default=1),
            preserve_default=False,
        ),
    ]
