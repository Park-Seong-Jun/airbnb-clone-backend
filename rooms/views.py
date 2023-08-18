from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


# Create your views here.


def say_hello(request):
    rooms = Room.objects.all()

    return render(
        request,
        "see_all_rooms.html",
        {
            "rooms": rooms,
            "title": "This page show all Rooms!",
        },
    )


def see_room(request, room_id):
    return HttpResponse(f"Room {room_id}")
