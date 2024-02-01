from celery import shared_task
import time


@shared_task
def start_processing(obj):
    """ Для обработки различных типов файлов можно использовать соответствующие библиотеки,
    например, Pillow для изображений или PyPDF2 для PDF-файлов """
    from files.models import File
    current_file = File.objects.get(id=obj['id'])
    extension = obj['file'].split('.')[-1].lower()
    if extension in ('jpg', 'jpeg', 'png', 'bmp'):
        time.sleep(20)  # simulation of processing
    elif extension in ('pdf', 'doc', 'docx', 'txt', 'rtf'):
        time.sleep(10)  # simulation of processing
    current_file.processed = True
    current_file.save()
