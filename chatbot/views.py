from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from openai import Completion

class GenerateTextView(APIView):
    def get(self, request):
        # Get URLs from the request or use default ones if not provided
        urls = request.GET.getlist('urls')
        if not urls:
            urls = [
                "https://data.worldbank.org/indicator/SI.POV.DDAY?locations=1W-BR",
                "https://data.worldbank.org/indicator/IT.NET.USER.ZS?locations=1W-BR",
                "https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS?locations=1W-BR"
            ]

        # Get user question from the request
        user_question = request.GET.get('question', 'What impact does climate change have on the environment?')

        # Collect data from each URL
        summaries = []
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                summary = data.get('summary', 'No summary available.')
                summaries.append(summary)
            else:
                summaries.append(f"Failed to retrieve data from {url}")

        # Create a combined prompt with all summaries and the user's question
        combined_prompt = " ".join(summaries) + " " + user_question

        # Generate text using OpenAI's GPT-3
        try:
            gpt_response = Completion.create(
                engine="text-davinci-003",
                prompt=combined_prompt,
                max_tokens=250
            )
            generated_text = gpt_response.choices[0].text.strip()
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"generated_text": generated_text})
