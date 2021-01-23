# Generated by Django 2.2 on 2021-01-23 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210123_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authtoken',
            name='type',
            field=models.CharField(choices=[('register', 'Регистрация'), ('password_reset', 'Восстановление пароля')], default='register', max_length=20, verbose_name='Тип токена'),
        ),
    ]