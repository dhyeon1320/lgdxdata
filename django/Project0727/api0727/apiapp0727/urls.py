from django.urls import path
from .views import getAPI, postAPI, bookAPI


urlpatterns = [
    # /example/get/ 요청이 오면 helloAPI 함수가 처리
    path("get/", getAPI),
    # /example/post/ 요청이 오면 postAPI 함수가 처리
    path("post/", postAPI),
    # bid 받아서 데이터 1개
    path("post/<int:bid>/",bookAPI )
]