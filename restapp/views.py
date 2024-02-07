from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import books
from .serializers import ItemSerializer
#post
class ItemListCreate(generics.ListCreateAPIView):
    queryset = books.objects.all()
    serializer_class = ItemSerializer
#get
class Itemview(generics.ListAPIView):
    queryset = books.objects.all()
    serializer_class = ItemSerializer
#delete
class Itemdelete(generics.DestroyAPIView):
    queryset = books.objects.all()
    serializer_class = ItemSerializer
#update 
class Itemchange(generics.UpdateAPIView):
    queryset = books.objects.all()
    serializer_class = ItemSerializer


