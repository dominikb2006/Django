from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord


def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    date_dict = {"access_records": webpages_list}

    # return HttpResponse("Hello World!")
    # my_dict = {'insert_me': "Hello I am from first_appviewx.py"}
    return render(request, 'first_app/index.html', context=date_dict)


def index2(request):
    my_dict = {'insert_content': "Yo"}
    return render(request, 'first_app/index2.html', context=my_dict)
