from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import CarViewSetGeneric,FirstBazdidViewSetGeneric,MonthBazdidViewSetGeneric,AnbarViewSetGeneric

router = DefaultRouter()
router.register('car', CarViewSetGeneric, basename='car')
router.register('firstbazdid', FirstBazdidViewSetGeneric, basename='firstbazdid')
router.register('monthbazdid', MonthBazdidViewSetGeneric, basename='monthbazdid')
router.register('anbar', AnbarViewSetGeneric, basename='anbar')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

]
