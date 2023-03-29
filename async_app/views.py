from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from celery.result import AsyncResult

from tetsuya_site.tasks import add

from .models import VideoFile
from .serializers import VideoFileSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def celery_test(request):
    task_id = add.delay(5, 5)

    result = AsyncResult(task_id)
    print("result:", result, " : ", result.state, " : ", result.ready())

    return JsonResponse({"result": "ok"})


@permission_classes([AllowAny])
class VideoFileViewSet(viewsets.ModelViewSet):
    queryset = VideoFile.objects.all()
    serializer_class = VideoFileSerializer
