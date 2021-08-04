from re import U
from typing import List
from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from my_app.models import Musician,Album
from my_app import forms
from .forms import MusicianForm



# Create your views here.



def home(request):
    singer_list = Musician.objects.order_by('first_name')
    context = {
        'singer_in_template':singer_list,
    }
    return render(request, 'my_app/index.html',context)


def form(request):


    obj_form = forms.user_form()
    context = {
        'obj_in_template':obj_form,
    }

    if request.method == 'POST':
        obj_form = forms.user_form(request.POST)

        if obj_form.is_valid():
            user_name = obj_form.clean_data['user_name']
            user_email = obj_form.cleaned_data['user_email']

            context.update({'user_name':user_name})
            context.update({'user_email':user_email})
            context.update({'form_submitted':"Yes"})


    return render(request,"my_app/form.html",context)





class Musicians(ListView):
    model = Musician



def single_musician_detail(request,pk):
    singer_id = pk
    artist_object = Musician.objects.get(pk = singer_id)
    
    context = {
        'artist':artist_object,

    }
    return render(request, "my_app/musician_detail.html",context)


class AlbumsOgli(ListView):
    model = Album


def addMusician(request):
    musician_list = Musician.objects.all()
    context = {
        'singer_list':musician_list,
    }


    if request.method == "POST":
        if request.POST.get("f_name") and request.POST.get("l_name") and request.POST.get("tool"):
            '''semir = Musician()
            semir.first_name = request.POST.get("f_name")
            semir.last_name = request.POST.get("l_name")
            semir.tool = request.POST.get("tool")'''

            semir = Musician(first_name=request.POST.get("f_name"),last_name=request.POST.get("l_name"), tool = request.POST.get("tool"))
            semir.save()

            return render(request, "my_app/add_musician.html",context)

    else:
        return render(request,"my_app/add_musician.html",context)


def addAlbum(request):
    if request.method == "POST":
        if request.POST.get("artist_name") and request.POST.get("album_name") and request.POST.get("date") and request.POST.get("num_stars"):
            n_album = Album()
            x = Musician.objects.get(first_name = request.POST.get(  "artist_name"))
            n_album.artist = x
            n_album.name = request.POST.get("album_name")
            n_album.rel_date = request.POST.get("date")
            n_album.num_stars = request.POST.get("num_stars")

            n_album.save()
            return render(request,"my_app/add_album.html")
    else:
        return render(request,"my_app/add_album.html")




def detailSinger(request):
    singer_list = Musician.objects.all()
    url = []
    for x in singer_list:
        url.append(x.first_name + "_"+x.last_name)
    context = {
        "object_list":singer_list,
        "urls_list":url,
    }
    return render (request,"my_app/detail_singer.html",context)


def detailMusicianName(request,namos):
    name_surname = namos.split("-")
    x = Musician.objects.get(first_name= name_surname[0])
    context={
        "obj":x,
        'namos':namos,
    }
    return render(request, "my_app/detail-musicianname.html",context)
