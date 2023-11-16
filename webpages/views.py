from django.shortcuts import render
import os

def test_index(request):
    return render(request, 'webpages/test_index.html', {'OPENAI_API_KEY': os.environ.get('OPENAI_API_KEY')})
