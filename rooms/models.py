from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    address = models.CharField(
        max_length=250,
    )
    room_kind = models.CharField(max_length=150, choices=RoomKindChoices.choices)
    price = models.PositiveIntegerField()
    toilet_num = models.PositiveIntegerField()
    room_num = models.PositiveIntegerField()
    pet_friendly = models.BooleanField(
        default=True,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )

    description = models.TextField()


class Amenity(CommonModel):

    """Amenity Model Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )