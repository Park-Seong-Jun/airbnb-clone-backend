from rest_framework.serializers import ModelSerializer
from .models import Wishlist
from rooms.serializers import RoomListSerializer


class WishlistSerializer(ModelSerializer):
    rooms = RoomListSerializer(many=True, read_only=True)

    # Experience에 대해서 room과 동일하게 Short cut Serializer 생성 및 적용
    class Meta:
        model = Wishlist
        fields = [
            "pk",
            "name",
            "rooms",
            "experiences",
        ]
