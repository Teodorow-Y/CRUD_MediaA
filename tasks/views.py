from rest_framework import viewsets
from .serializer import CheckSerializer
from .models import mediaDB

# Create your views here.


class MediaViewSet(viewsets.ModelViewSet):
    serializer_class = CheckSerializer
    queryset = mediaDB.objects.all()