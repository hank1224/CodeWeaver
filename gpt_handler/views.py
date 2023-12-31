from django.shortcuts import render
from openai import OpenAI
from django.http import HttpResponse

def test_API(request):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
    )

    return_str = str(completion.choices[0].message.content) + "，有說英文代表成功"
    return HttpResponse(return_str)