from django.http import HttpResponse


def first(request):
    return HttpResponse("First Page!")
