from AppTwo.models import User
from django.shortcuts import render

from AppTwo.forms import UserForm


def index(request):
    # return HttpResponse("<em>My Second App </em>")
    index_dict = {'index_insert': "Yup, Its index"}
    return render(request, 'AppTwo/index.html', context=index_dict)


def help(request):
    help_dict = {'help_insert': "Sorry, i Can't help you :("}
    return render(request, 'AppTwo/help.html', context=help_dict)


def users(request):
    webpages_list = User.objects.order_by("FirstName")
    users_dict = {"users_list_insert": webpages_list,
                  'users_insert': "THERE IS A LIST! LIST I SAID!"}
    return render(request, 'AppTwo/users.html', context=users_dict)


def signup(request):
    form = UserForm()
    signup_dict = {"signup_form": form}

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            # ZROB COS
            form.save(commit=True)
            print("VALIDATION SUCCESS")
            print("FIRST NAME: " + form.cleaned_data['FirstName'])
            print("LAST NAME: " + form.cleaned_data['LastName'])
            print("EMAIL: " + form.cleaned_data['Email'])
            # print("VERIFY EMAIL: " + form.cleaned_data['verify_email'])
            return index(request)

        else:
            print('ERROR FORM INVALID / Email, not unique /')

    return render(request, 'AppTwo/signup.html', context=signup_dict)
