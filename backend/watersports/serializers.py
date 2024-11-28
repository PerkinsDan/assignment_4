from rest_framework import serializers
from .models import Boat

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ('id', 'boat_class', 'manufacturer', 'adult_capacity', 'child_capacity')