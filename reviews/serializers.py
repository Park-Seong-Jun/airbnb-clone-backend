from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import ShortUserSerializer


class ReviewSerializer(ModelSerializer):
    user = ShortUserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "pk",
            "user",
            "payload",
            "rating",
        ]
