# Generated by Django 2.1.7 on 2019-03-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refurbco', '0002_auto_20190326_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.TextField(max_length=20),
        ),
    ]