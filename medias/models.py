from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.ImageField()
    description = models.CharField(max_length=144)
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="photos",
    )

    def __str__(self):
        return "photo file"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="videos",
    )

    def __str__(self):
        return "video file"
