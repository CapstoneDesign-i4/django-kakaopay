# Generated by Django 3.1.3 on 2022-04-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchat', '0028_product_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='web_result',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
