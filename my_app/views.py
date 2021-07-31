from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Musician,Album
# Create your views here.

def home(request):
    singer_list = Musician.objects.order_by('first_name')
    context = {
        'singer_in_template':singer_list,
    }
    return render(request, 'my_app/index.html',context)


def form(request):
    return render(request,"my_app/form.html")