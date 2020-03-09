from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello World!")
    my_dict = {'insert_me': "Hello I am from first_appviewx.py"}
    return render(request, 'first_app/index.html', context=my_dict)
