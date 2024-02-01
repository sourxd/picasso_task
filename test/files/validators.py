from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size
    if filesize > 10485760:
        raise ValidationError("Вы не можете загружать файлы больше 10Mb")
    else:
        return value
