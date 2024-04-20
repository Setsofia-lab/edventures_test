from django.http import HttpResponse

from . import urls


def chatbot(request):
    return HttpResponse("Hello, world. You're welcome to the chatbot. ask your questions")