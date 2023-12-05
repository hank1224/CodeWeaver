from django.test import TestCase

# Create your tests here.

# 測試OpenAI API
class TestGptHandler(TestCase):
    def test_gpt_handler(self):
        response = self.client.get('/gpt_handler/test_API')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gpt_handler/test_API.html')