from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def ajax(request):
    return render(request, "ajax.html")

# GET 요청만 처리
@api_view(['GET'])
def getAPI(request):
    return Response("HELLO REST API")

from .serializers import BookSerializer
from rest_framework import status
from .models import Book

@api_view(['POST', 'GET'])
def postAPI(request):
    # 전송 방식 확인 방법 - request.method 확인
    if request.method == 'GET':
        # 전체 데이터 가져오기
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        print("1") # 이 코드가 실행 안 되면 URL과 method가 연결되지 않은 것
        # 클라이언트가 전송한 데이터를 model이 사용할 수 있는 데이터로 변환
        serializer = BookSerializer(data = request.data)
        print("2") # 이 코드가 안 되면 Serializable 실패한 것
        # 유효성 검사
        if serializer.is_valid():
            print("3") # 이 코드가 안 되면 이름이 잘못 된 것
            serializer.save()  # 데이터 저장
            # 성공했을 때 전송한 데이터를 다시 전송
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #실패했을 때
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 기본 키로 데이터 1개 가져옴 - 없으면 404 에러 발생
from rest_framework.generics import get_object_or_404
@api_view(['GET'])
def bookAPI(request, bid):
    # 기본 키로 데이터 1개 가져오기
    book= get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


