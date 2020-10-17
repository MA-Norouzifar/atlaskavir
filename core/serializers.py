from rest_framework import serializers
from .models import Car, FirstBazdid, MonthBazdid, Anbar

class AnbarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anbar
        fields = '__all__'

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'Name', 'Famil','mobile', 'slug', 'Type_Car',
                  'Number_Car', 'Plak_Car', 'Model_Car', 'created', 'updated']
        read_only_fields = ['slug']
        # fields = ['id', 'Name', 'Famil', 'Type_Car', 'Number_Car', 'Plak_Car']


class FirstBazdidSerializers(serializers.ModelSerializer):
    class Meta:
        model = FirstBazdid
        fields = '__all__'

class monthBazdidSerializers(serializers.ModelSerializer):
    class Meta:
        model = MonthBazdid
        fields = '__all__'
