from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# views handles various webpages

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>Hello World</h1>") # html code
    return render(request, "home.html",{})