from django.http import HttpResponse
from . import urls

def index(request):
    return HttpResponse("Hello! Welcome to edventures chatbot")
