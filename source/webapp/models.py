from django.contrib.auth import get_user_model
from django.db import models

MESSAGE_STATUS_CHOICES = (
    ('inbox', 'Входящие'),
    ('outbox', 'Исходящие')
)


class Friend(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_friends',
                             verbose_name='Пользователь')
    friend = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='friend_friends',
                               verbose_name='Друг')

    def __str__(self):
        return f'{self.user} - {self.friend}'

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'


class Message(models.Model):
    froms = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='from_messages',
                              verbose_name='Сообщение')
    whom = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='whom_messages',
                             verbose_name='Сообщение')
    text = models.TextField(max_length=1000, blank=True, null=True, verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.froms} - {self.whom}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
