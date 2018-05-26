from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Image
from .serializers import UserImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UserImageSerializer

