from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.pagination import LimitOffsetPagination

from .models import Image
from .serializers import UserImageSerializer, Base64ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = UserImageSerializer
    pagination_class = LimitOffsetPagination


class Base64ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    parser_classes = (JSONParser,)
    serializer_class = Base64ImageSerializer
    pagination_class = LimitOffsetPagination
