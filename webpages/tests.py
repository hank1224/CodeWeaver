from django.test import TestCase

# Create your tests here.

# 測試圖片庫讀取 和 OpenAI API key讀取
class TestIndexView(TestCase):
    def test_index_view(self):
        response = self.client.get('/webpages/test_index')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'webpages/test_index.html')
        self.assertContains(response, 'OPENAI_API_KEY')