from django.contrib.auth.models import User
from rest_framework import status, generics, routers, serializers, viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, SectionSerializer, BookSerializer

import custom_utils.helper_functions as utils
from .models import Book, Section


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class SectionViewSet(viewsets.ModelViewSet):
    """
    List all workers, or create a new worker.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    List all workkers, or create a new worker.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_date']