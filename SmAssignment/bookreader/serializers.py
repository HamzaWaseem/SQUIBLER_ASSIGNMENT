
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Section, Book


# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Section
        fields = ("id", "book", "heading", "content", "parent_section")
        extra_kwargs = {'parent_section': {'required': False}}

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        ordering = ['-id']
        model = Book
        fields = ("id", "title", "description", "user")
        extra_kwargs = {'user': {'required': False}}