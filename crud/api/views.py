from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from movie.models import Movie


def get_and_create_movies(request):
    if request.method == "GET":
        return HttpResponse(serialize('json', Movie.objects.all()), content_type="application/json")
    if request.method == "POST":
        pass
    else:
        return HttpResponse('[]', content_type="application/json", status=403)