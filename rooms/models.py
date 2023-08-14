from django.db import models
from common.models import CommonModel
from django.db.models import Avg


# Create your models here.
class Room(CommonModel):

    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        max_length=200,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
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
    kind = models.CharField(
        max_length=150,
        choices=RoomKindChoices.choices,
    )
    price = models.PositiveIntegerField()
    toilet_num = models.PositiveIntegerField()
    room_num = models.PositiveIntegerField()
    pet_friendly = models.BooleanField(
        default=True,
    )
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")

    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    def rating(rooms):
        reviews_avg = rooms.reviews.aggregate(Avg("rating"))["rating__avg"]

        if reviews_avg == None:
            return "No Review"

        return round(reviews_avg, 2)


class Amenity(CommonModel):

    """Amenity Model Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
