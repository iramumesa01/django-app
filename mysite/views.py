from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! This is my homepage.")
