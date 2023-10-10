from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from rest_framework.exceptions import NotFound
from .serializers import WishlistSerializer
from .models import Wishlist
from rooms.models import Room


class Wishlists(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(
            wishlists, many=True, context={"request": request}
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            Response(serializer.errors)


class WishlistDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(wishlist, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        wishlist = self.get_object(pk)
        serializer = WishlistSerializer(wishlist, data=request.data, partial=True)
        if serializer.is_valid():
            wishlist = serializer.save()
            return Response(WishlistSerializer(wishlist).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        wishlist = self.get_object(pk)
        wishlist.delete()
        return Response(HTTP_204_NO_CONTENT)


class WishlistToggle(APIView):
    def get_list(self, pk):
        try:
            return Wishlist.objects.get(pk=pk)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        wishlist = self.get_list(pk=pk)

        room = self.get_room(pk=room_pk)
        # 리스크 내에서 특정 데이터의 존재 유무를 확인하는 알고리즘을 사용하는 메서드 확인 필요(exist?)
        if room in wishlist.rooms.all():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)
        return Response(HTTP_200_OK)
