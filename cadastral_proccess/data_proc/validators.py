import re

from django.core.exceptions import ValidationError


def validate_cadastral(value):
    """Валидация кадастрового номера."""
    if not re.fullmatch(r'^\d{2}:\d{2}:\d{6}:\d{3}$', value):
        raise ValidationError(
            'Кдастровый номер должен соответствовать виду: ХХ:ХХ:ХХХХХХ:ХХХ.'
        )
    return value


def validate_coordinates(value):
    """Валидация широты и долготы."""
    if value < -90 or value > 90:
        raise ValidationError('Значение должно быть между -90 и 90.')
    return value


def validate_task(value):
    """Валидация id задачи."""
    if not re.fullmatch(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$',
        value
    ):
        raise ValidationError('Неверный формат данных! '
                              'Должно соответствовать uuid4.')
    return value
