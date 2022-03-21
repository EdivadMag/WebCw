# Generated by Django 3.2.12 on 2022-03-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='000', max_length=3, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2022)),
            ],
        ),
    ]