# Generated by Django 3.2.3 on 2022-11-04 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appSITUweb', '0002_auto_20221104_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pasajero',
            name='telefono',
        ),
    ]
