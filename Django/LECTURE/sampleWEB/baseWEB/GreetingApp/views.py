from django.shortcuts import render, HttpResponse

# Create your views here.
def hi(request) :
    return HttpResponse ('섭이와 함께하는 장고 웹')

