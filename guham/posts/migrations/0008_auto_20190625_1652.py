# Generated by Django 2.1.8 on 2019-06-25 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190625_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='study_place',
            field=models.CharField(choices=[('강남역', '강남역'), ('교대역', '교대역'), ('역삼역', '역삼역')], max_length=10),
        ),
    ]
