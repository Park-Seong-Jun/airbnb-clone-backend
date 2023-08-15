from django.contrib import admin
from .models import Review


# Register your models here.
class word_filter(admin.SimpleListFilter):
    title = "Filtering by word"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("awesome", "Awesome"),
            ("good", "Good"),
        ]

    def queryset(self, request, reviews):
        # word_filter = request.GET["word"]
        word = self.value()
        print(type(word))
        print(self.value)
        if word:
            return reviews.filter(payload__icontains=word)
        else:
            reviews


class rating_filter(admin.SimpleListFilter):
    title = "Filtering by rating"
    parameter_name = "evaluating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        word = self.value()

        if word == "good":
            return reviews.filter(rating__gte=3)
        elif word == "bad":
            return reviews.filter(rating__lt=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        word_filter,
        rating_filter,
        "rating",
        "room__pet_friendly",
    )
