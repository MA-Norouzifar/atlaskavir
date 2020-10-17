from django.shortcuts import render
from rest_framework import mixins
from rest_framework import viewsets
# Create your views here.

from .serializers import CarSerializers,FirstBazdidSerializers,monthBazdidSerializers, AnbarSerializers
from .models import Car,FirstBazdid, MonthBazdid, Anbar


class CarViewSetGeneric(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

class FirstBazdidViewSetGeneric(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = FirstBazdid.objects.all()
    serializer_class = FirstBazdidSerializers


class MonthBazdidViewSetGeneric(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = MonthBazdid.objects.all()
    serializer_class = monthBazdidSerializers

class AnbarViewSetGeneric(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Anbar.objects.all()
    serializer_class = AnbarSerializers