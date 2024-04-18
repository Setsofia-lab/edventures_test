from django.urls import path
from .views import GenerateTextView
from . import views

urlpatterns = [
    path('chatbot/', GenerateTextView.as_view(), name='chatbot/'),
]
