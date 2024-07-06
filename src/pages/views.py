from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# views handles various webpages

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>Hello World</h1>") # html code
    return render(request, "home.html",{})

def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>Hello World</h1>") # html code
    return render(request, "contact.html",{})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about me",
        "my_number": 12345678,
        "my_list": [1,23,45,678]
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Socials</h1>") # html code
