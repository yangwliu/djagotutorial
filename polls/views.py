# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world!")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def say_hello(request):
    data = [{"id": i, "name": i + 1} for i in range(10)]
    return render(request, "polls/hello.html", {"latest_question_list": data})

