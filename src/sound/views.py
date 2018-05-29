from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import LimitOffsetPagination

from .models import Sound
from .serializers import SoundSerializer


class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer
    parser_classes = (MultiPartParser, FormParser)
    pagination_class = LimitOffsetPagination
