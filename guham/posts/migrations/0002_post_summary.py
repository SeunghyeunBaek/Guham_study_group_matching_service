# Generated by Django 2.1.8 on 2019-06-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='summary',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
