# Generated by Django 4.1.7 on 2023-03-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180, verbose_name='Title')),
                ('description', models.TextField(max_length=256, verbose_name='Description')),
            ],
        ),
    ]
