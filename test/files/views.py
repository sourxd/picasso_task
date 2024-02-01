from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from files.models import File
from files.serializers import FilesSerializer
from files.tasks import start_processing


# ------------------- api ------------------


class FilesView(APIView):
    """ List files """
    def get(self, request):
        queryset = File.objects.all()
        serializer = FilesSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer.data)


class UploadView(APIView):
    """ Upload page """
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FilesSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            start_processing.delay(serializer.data)  # start task
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
