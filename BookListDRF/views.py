from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Books
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.
class BookView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    
class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer