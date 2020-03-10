from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User


def index(request):
    # return HttpResponse("<em>My Second App </em>")
    index_dict = {'index_insert': "Yup, Its index"}
    return render(request, 'AppTwo/index.html', context=index_dict)


def help(request):
    help_dict = {'help_insert': "Sorry, i Can't help you :("}
    return render(request, 'AppTwo/help.html', context=help_dict)


def users(request):
    users_dict = {'users_insert': "THERE IS A LIST! LIST I SAID!"}
    return render(request, 'AppTwo/users.html', context=users_dict)


def userslist(request):
    webpages_list = User.objects.order_by("FirstName")
    list_dict = {"users_list_insert": webpages_list}
    return render(request, 'AppTwo/users.html', context=list_dict)
