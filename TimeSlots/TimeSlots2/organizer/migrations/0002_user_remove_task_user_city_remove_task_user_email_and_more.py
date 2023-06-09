# Generated by Django 4.1.7 on 2023-03-18 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_user_surname', models.CharField(help_text='Введите фамилию', max_length=20, verbose_name='user_surname')),
                ('field_user_name', models.CharField(help_text='Введите имя', max_length=20, verbose_name='user_name')),
                ('field_user_name2', models.CharField(help_text='Введите отчество', max_length=20, verbose_name='user_name2')),
                ('field_user_position', models.CharField(help_text='Введите должность', max_length=20, verbose_name='user_position')),
                ('field_user_org_name', models.CharField(help_text='Введите название организации', max_length=20, verbose_name='user_org_name')),
                ('field_user_city', models.CharField(help_text='Введите город', max_length=20, verbose_name='user_city')),
                ('field_user_street', models.CharField(help_text='Введите название улицы', max_length=20, verbose_name='user_street')),
                ('field_user_hauce', models.CharField(help_text='Введите номер дома, корпус и т.д.', max_length=20, verbose_name='user_hauce')),
                ('field_user_phone', models.CharField(help_text='Введите номер телефона', max_length=20, verbose_name='user_phone')),
                ('field_user_email', models.CharField(help_text='Введите электронную почту', max_length=20, verbose_name='user_email')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_city',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_hauce',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_name2',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_org_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_phone',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_position',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_street',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user_surname',
        ),
    ]
