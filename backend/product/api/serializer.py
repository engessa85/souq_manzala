from dataclasses import fields
from rest_framework import serializers
from product.models import Persons,MainSlider

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ['idvalue', 'email', 'first_name', 'last_name','avatar']


class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ['productor_name', 'avatar']