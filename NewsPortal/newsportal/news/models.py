from django.db import models


class Articles(models.Model):
    title=models.CharField('Название',max_length=100)
    first_words = models.CharField('Начало', max_length=255)
    text_feild = models.TextField('')
    date=models.DateField('Дата публикации')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'