# Generated by Django 3.2.8 on 2021-10-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
