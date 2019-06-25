# Generated by Django 2.2.2 on 2019-06-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.EmailField(max_length=255, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='full_name')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
