from django.shortcuts import render

# Create your views here.
# 모델 클래스 import
from webapplication.models import Item

def index(request):
    data1 = Item.objects.all()
    for i in data1:
        print(i.itemname)

    # 전체 데이터 가져오기 - html
    #data = Item.objects.all()

    data = Item.objects.all()
    return render(request, "index.html", {"data": data})

# url 뒤에 붙은 parameter는 두 번째 매개변수 이용해서 가져옴
def detail(request, itemid):
    item = Item.objects.get(itemid = itemid)
    return render(request, 'detail.html', {'item':item})
