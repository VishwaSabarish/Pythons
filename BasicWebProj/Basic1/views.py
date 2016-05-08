from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album


# Create your views here.
def index(request):
    album_list = Album.objects.all()
    template = loader.get_template('Basic1/index.html')
    context = {
        'album_list': album_list,
    }
    # html = ''
    # for album in album_list:
    #     url = '/Basic/' + str(album.id) + '/'
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br />'
    # return HttpResponse(html)
    return HttpResponse(template.render(context, request))


def details(request, album_id):
    return HttpResponse("<h2> details for: " + str(album_id) + "</h2>")