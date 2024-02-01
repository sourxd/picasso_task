from django.db import models
from files.tasks import start_processing

from files.validators import validate_file_size


class File(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Файл', validators=[validate_file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    processed = models.BooleanField(default=False, editable=False, verbose_name='Обработан/Не обработан')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return f'{self.file} ---- {"Обработан" if self.processed else "Не обработан"}'
