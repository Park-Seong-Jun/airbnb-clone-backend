from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializer import ShortUserSerializer
from categories.serializer import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = [
            "name",
            "description",
        ]


class RoomDetailSerializer(ModelSerializer):
    owner = ShortUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "pk",
            "name",
            "country",
            "city",
            "price",
        ]

    def create(self, validated_data):
        return Room.objects.create(**validated_data)
