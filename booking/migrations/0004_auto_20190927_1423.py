# Generated by Django 2.2.4 on 2019-09-27 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190927_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='customer',
            new_name='email',
        ),
    ]
