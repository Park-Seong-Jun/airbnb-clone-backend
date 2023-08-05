from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    # Wishlist model definition
    name = models.CharField(
        max_length=150,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    rooms = models.ManyToManyField(
        "rooms.Room",
        blank=True,
    )
    experiences = models.ManyToManyField(
        "experiences.Experience",
        blank=True,
    )

    def __str__(self):
        return self.name
