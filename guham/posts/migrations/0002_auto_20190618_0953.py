# Generated by Django 2.1.8 on 2019-06-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='study_category',
            field=models.CharField(choices=[('python', 'Python'), ('r', 'R'), ('java', 'Java')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='study_day',
            field=models.CharField(choices=[('주1회', '주1회'), ('주2회', '주2회'), ('주3회', '주3회'), ('협의', '협의')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='study_place',
            field=models.CharField(choices=[('강남', '강남역'), ('교대', '교대역'), ('역삼', '역삼역')], max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='study_time',
            field=models.CharField(choices=[('1hour', '1hour'), ('2hour', '2hour'), ('3hour', '3hour')], max_length=10),
        ),
    ]
