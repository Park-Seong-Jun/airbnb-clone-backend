from rest_framework.serializers import ModelSerializer
from .models import User


class ShortUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "avatar",
            "name",
        ]
