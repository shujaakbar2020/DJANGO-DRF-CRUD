from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, BookSerializer
from .models import Book


class UserViewSet(viewsets.ModelViewSet):
    """
        API endpoint allow users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_class = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
        API endpoint allow Groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions_class = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_class = [permissions.IsAuthenticated]


class CreateBook(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permissions_class = [permissions.IsAuthenticated]
