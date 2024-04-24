from django.http import HttpResponse

from . import urls
from . import models

from .models import user_question,bot_response


def chatbot(request):
    input = question
    output = response
    return HttpResponse(input, output)

def question(request, user_question):
    return HttpResponse("Input your question here." % user_question)


def response(request, bot_response):
    response = ("Bot response - " % bot_response)
    return HttpResponse(response % bot_response)
