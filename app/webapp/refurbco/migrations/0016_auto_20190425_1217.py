# Generated by Django 2.1.7 on 2019-04-25 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refurbco', '0015_auto_20190425_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='repairticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='refurbco.RepairTicket'),
        ),
    ]