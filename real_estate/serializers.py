from rest_framework import serializers

from .models import Address, Property

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        # fields = "__all__"
        exclude = ["id"]

class PropertySerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Property
        fields = "__all__"
