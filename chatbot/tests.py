from django.urls import reverse
from django.test import TestCase
from unittest.mock import patch, MagicMock

class GenerateTextTests(TestCase):
    @patch('chatbot.views.requests.get')
    @patch('chatbot.views.Completion.create')
    def test_generate_text_from_api(self, mock_create, mock_get):
        # Setup mock for requests.get to handle multiple URLs
        mock_response1 = MagicMock()
        mock_response1.status_code = 200
        mock_response1.json.return_value = {"summary": "Summary from URL 1"}

        mock_response2 = MagicMock()
        mock_response2.status_code = 200
        mock_response2.json.return_value = {"summary": "Summary from URL 2"}

        mock_get.side_effect = [mock_response1, mock_response2]

        # Setup mock for Completion.create from OpenAI
        mock_choice = MagicMock()
        mock_choice.text.strip.return_value = 'Generated response based on summaries and user question'
        mock_openai_response = MagicMock()
        mock_openai_response.choices = [mock_choice]
        mock_create.return_value = mock_openai_response

        # Prepare URL and query parameters
        url = reverse('generate_text')
        url += '?question=How many people are living in poversty in Brazil?&urls=https://data.worldbank.org/indicator/SI.POV.DDAY?locations=1W-BR"'
        
        # Execute test
        response = self.client.get(url)
        
        # Check results
        self.assertEqual(response.status_code, 200)
        self.assertIn('Generated response based on summaries and user question', response.json()['generated_text'])
