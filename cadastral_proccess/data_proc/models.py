from django.db import models

from .validators import validate_cadastral


class CadastralData(models.Model):
    """Модель кадастровых данных."""

    cadastral_number = models.CharField(max_length=16,
                                        validators=[validate_cadastral],
                                        verbose_name='Кадастровый номер')
    longitude = models.DecimalField(max_digits=9,
                                    decimal_places=6,
                                    verbose_name='Долгота')
    latitude = models.DecimalField(max_digits=9,
                                   decimal_places=6,
                                   verbose_name='Широта')
    result = models.BooleanField(null=True, verbose_name='Результат')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        ordering = ['-date']
        verbose_name = 'Кадастровые данные'

    def __str__(self):
        return f'{self.cadastral_number}: {self.result}'
