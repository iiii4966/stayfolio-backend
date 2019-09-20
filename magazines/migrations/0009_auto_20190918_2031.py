# Generated by Django 2.2.4 on 2019-09-18 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0008_auto_20190918_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_type', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'content_type',
            },
        ),
        migrations.AlterField(
            model_name='contents',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazines.ContentType'),
        ),
    ]
