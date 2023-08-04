from django.db import models
from common.models import CommonModel


# Create your models here.
class Category(CommonModel):
    """Category model definition"""

    class CategoryKindChoices(models.TextChoices):
        ROOM = ("room", "Room")
        EXPERIENCE = ("experience", "Experience")

    name = models.CharField(
        max_length=50,
    )
    kind = models.CharField(max_length=10, choices=CategoryKindChoices.choices)

    def __str__(self):
        return f"{self.kind} : {self.name}"

    class Meta:
        verbose_name_plural = "Categories"
