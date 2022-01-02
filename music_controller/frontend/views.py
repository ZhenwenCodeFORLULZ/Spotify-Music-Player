from django.shortcuts import render

# Create your views here.
def index(request, *args, **kwargs):
    return render(request,'frontend/index.html')
    #allow us to render this react template, by taking the request and taking the template and return to whereever we sent the request
