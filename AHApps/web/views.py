from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    data = {
        'name': "brijesh gondaliya",
        'age': 27,
        'city': "Surat"
    }
    return render(request, 'web/index.html', {'data':data})

def mydata(request):
    return HttpResponse("This is a my data")

def mybiodata(request):
    data = {
        'name': "brijesh gondaliya",
        'age': 27,
        'city': "Surat"
    }
    return HttpResponse(data)