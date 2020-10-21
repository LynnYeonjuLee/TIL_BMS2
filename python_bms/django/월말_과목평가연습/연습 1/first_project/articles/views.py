# django imports style guide
# 1. standard library
# 2. 3rd party
# 3. Django
# 4. local django
import random
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick':pick, 
    }
    return render(request, 'dinner.html', context)


# variable routing 
def hello(request, name):
    context = {
        'name':name
    }
    return render(request, 'hello.html', context)


def dtl_practice(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    empty_list = []
    context = {
        'menus':menus,
        'empty_list':empty_list
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # throw 에서 보낸 form 데이터를 받기
    # print(request.GET)
    # request.GET['name'] # 데이터 없으면 서버가 끝나버림
    message = request.GET.get('name') # 없으면 None 값 출력
    context = {
        'message': message, 
    }
    return render(request, 'catch.html', context)