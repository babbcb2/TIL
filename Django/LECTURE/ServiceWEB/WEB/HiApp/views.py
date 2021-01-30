from django.shortcuts import render, HttpResponse

# Create your views here.

def index (request) :
    # return HttpResponse ('*** 여기는 시작페이지 입니다 ***')
    context = {'ment' : '죄송합니다~ 어려워서요 ㅜ'}
    return render(request, 'Hi/index.html', context)

def baseball (request) :
    return  HttpResponse ('*** 여기는 야구 입니다 ***')

