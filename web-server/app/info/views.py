from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .custompermissions import IsAdminOrReadonly

from .serializers import InfoSerializer
from .models import Info
# Create your views here.

class InfoListAPiView(ListCreateAPIView):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    permission_classes = (IsAdminOrReadonly)

class InfoDetailAPiView(ListCreateAPIView):
    serializer_class = InfoSerializer
    queryset = Info.objects.all()
    permission_classes = (IsAdminOrReadonly)
    lookup_url_kwarg = 'disease_id'
