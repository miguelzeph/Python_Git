from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):

    #return HttpResponse("HELLO WORLD")
    return render(request, 'home.html', {'usuario': "FULANO DE TAL"})

def contact(request):
    return render(request, 'contact.html')




