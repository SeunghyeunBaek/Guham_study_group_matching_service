# Generated by Django 2.1.8 on 2019-06-26 07:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0008_auto_20190625_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='applicant',
            field=models.ManyToManyField(related_name='applied_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
