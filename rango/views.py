from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    #return HttpResponse("Rango says: Hello world! <a href='/rango/about'>About</a>a>")
    return render(request, 'rango/index.html', context_dict)
