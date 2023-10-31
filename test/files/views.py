import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from files.models import File
from files.forms import FileForm
from files.serializers import FilesSerializer
from files.tasks import start_processing


# ------------------- api ------------------


class FilesView(APIView):
    def get(self, request):
        queryset = File.objects.all()
        serializer = FilesSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer.data)


class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FilesSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            start_processing.delay(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# ------------------- visual ------------------
def files_view(request):
    file_list = File.objects.all()
    context = {
        'title': 'Список файлов',
        'list': file_list,
    }
    return render(request, os.path.join('files', 'list.html'), context)


def upload_view(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = FileForm()
    context = {
        'title': 'Загрузка файла',
        'form': form,
    }
    return render(request, os.path.join('files', 'up_form.html'), context)
