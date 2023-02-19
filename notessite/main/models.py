from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=250, verbose_name='название')
    task = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

















# Create your models here.
