from django.contrib.auth import get_user_model
from django.db import models


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

