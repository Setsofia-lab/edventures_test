"""
Database models.
"""
from django.conf import settings
from django.db import models


class user_question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class bot_response(models.Model):
    question = models.ForeignKey(user_question, on_delete=models.CASCADE)
    bot_text = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.bot_text
   