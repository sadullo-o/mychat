# Generated by Django 4.0.1 on 2022-12-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_video_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='data',
            field=models.CharField(max_length=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999),
        ),
    ]
