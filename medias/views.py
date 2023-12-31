from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Photo
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied


# Create your views here.
class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)

        if (request.user != photo.room.owner) or (
            request.user != photo.experience.host
        ):
            raise PermissionDenied

        photo.delete()
        return Response(status=HTTP_204_NO_CONTENT)
