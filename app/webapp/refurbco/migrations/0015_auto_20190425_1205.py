# Generated by Django 2.1.7 on 2019-04-25 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refurbco', '0014_auto_20190425_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='id',
            new_name='invoice_id',
        ),
    ]