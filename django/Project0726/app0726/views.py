from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# 요청 처리하는 함수의 매개변수는 request
# request 객체 안에 클라이언트에 대한 정보 저장되어 있음

def index(request):
    return HttpResponse("<p>Hello Django</p>")


def today(request):
    return render(request, "today.html")


def template(request):
    msg = "how are you? i'm fine thank you and you?"
    person = {"name":"kim", "age":53}
    # HTML에 데이터 전송하고자 하면 세번째 매개변수에 dictionary 만들어서 데이터 이름과 데이터 기재
    return render(request, "template.html", {"msg":msg, "person":person})

def template1(request):
    age = 54
    data = ["Stack", "Queue", "Deque", "LinkedList", "Tree", "Graph", "Array"]
    return render(request, "template1.html", {"age":age, "data":data})
