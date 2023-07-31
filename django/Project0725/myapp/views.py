from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # html 직접 작성해서 출력
    # return HttpResponse("<h1>Hello Django python</h1>")

    # html 파일 출력
    return render(request, 'index.html')

def hello(request):
    return HttpResponse("Hello")