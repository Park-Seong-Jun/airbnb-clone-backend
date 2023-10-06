from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
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

    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()
    reviews_counting = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return request.user == room.owner

    def get_reviews_counting(self, room):
        return room.counting_amenity()


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = [
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
            "is_owner",
        ]

    def get_rating(self, room):
        return room.rating()

    def get_is_owner(self, room):
        request = self.context["request"]
        return request.user == room.owner
