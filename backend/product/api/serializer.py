from dataclasses import fields
from rest_framework import serializers
from product.models import Persons

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ['idvalue', 'email', 'first_name', 'last_name','avatar']