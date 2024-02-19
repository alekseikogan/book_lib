import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.books.settings')
django.setup()

from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
