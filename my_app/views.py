from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Musician,Album
from my_app import forms
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
            user_name = obj_form.cleaned_data['user_name']
            user_email = obj_form.cleaned_data['user_email']

            context.update({'user_name':user_name})
            context.update({'user_email':user_email})
            context.update({'form_submitted':"Yes"})


    return render(request,"my_app/form.html",context)





def musician_list(request):
    singer_from_db = Musician.objects.all()
    count = Musician.objects.all().count()
    context = {
        'listo_singer':singer_from_db,
        'count_of_singer':count,
    }
    return render(request,"my_app/musician_list.html",context)