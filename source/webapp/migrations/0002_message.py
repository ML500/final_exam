# Generated by Django 2.2 on 2021-01-23 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Текст сообщения')),
                ('froms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_messages', to=settings.AUTH_USER_MODEL, verbose_name='Сообщение')),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whom_messages', to=settings.AUTH_USER_MODEL, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
