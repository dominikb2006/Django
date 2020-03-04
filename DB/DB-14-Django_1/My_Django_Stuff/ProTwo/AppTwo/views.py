from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("<em>My Second App </em>")
    index_dict = {'index_insert': "Yup, Its index"}
    return render(request, 'AppTwo/index.html', context=index_dict)

def help(request):
    help_dict = {'help_insert': "Sorry, i Can't help you :("}
    return render(request, 'AppTwo/help.html', context=help_dict)