# Generated by Django 4.1.2 on 2022-11-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_types_tovarlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korzina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('tovarnomi', models.CharField(max_length=100)),
                ('tovarnarxi', models.CharField(max_length=100)),
                ('tovarsoni', models.IntegerField()),
            ],
        ),
    ]
