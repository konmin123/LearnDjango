from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    message = models.TextField(default='', verbose_name='Текст сообщения')
    public = models.BooleanField(default=False, verbose_name='Опубликовать')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    update_ad = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):  # отображение человеко читаемой записи
        return f"Запись №{self.id}"

    class Meta:  # отображение человекочитаемой записи модели
        verbose_name = _("запись")
        verbose_name_plural = _("записи")

    # class Comment(models.Model):
    #     """"Комментарии и оценки к статьям"""
    #     class Rating(models.IntegerChoices):
    #         WITHOUT_RATING = 0, _("Без оценки")
    #         TERRIBLE = 1, _("Ужасно")
    #         BADLY = 2, _("Плохо")
    #         FINE = 3, _("Нормально")
    #         GOOD = 4, _("Хорошо")
    #         EXCELLENT = 5, _("Отлично")
    #
    #     author = models.ForeignKey(User, on_delete=models.CASCADE)
    #     note = models.ForeignKey(Note, on_delete=models.CASCADE)
    #     rating = models.ImageField(default=Rating.WITHOUT_RATING, choices=Rating)
