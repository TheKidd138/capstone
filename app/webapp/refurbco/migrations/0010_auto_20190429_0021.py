# Generated by Django 2.1.7 on 2019-04-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refurbco', '0009_repairticket_charged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='charged',
            field=models.TextField(max_length=20),
        ),
    ]
