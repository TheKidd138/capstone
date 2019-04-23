# Generated by Django 2.1.7 on 2019-04-23 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refurbco', '0005_remove_order_tax'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_number', models.TextField(max_length=5)),
                ('device', models.TextField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='PartType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdap', models.TextField(max_length=8)),
                ('part_type', models.TextField(max_length=16)),
                ('color', models.TextField(max_length=8)),
                ('quoteCost', models.TextField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='part_number',
            new_name='mdap',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='device_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='refurbco.Device'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='part_type',
            field=models.TextField(max_length=16),
        ),
    ]
