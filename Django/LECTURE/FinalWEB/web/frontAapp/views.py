from django.shortcuts   import render
from django.http        import  JsonResponse

# Create your views here.
def index (request) :
    print('request index -')
    return render (request, 'frontdemo.html')

def nonAjax (request) :
    print('request ajax nonAajx')
    list = [{ 'id': 'multicampus04', 'pwd': 'multicampus04'},
            {'id': 'multicampus05', 'pwd': 'multicampus05'}]
    return JsonResponse(list, safe=False)

def paramAjax (request) :
    id = request.POST['user_id']
    pwd = request.POST['user_pwd']
    print('ajax param -', id, pwd)

    list = [{ 'id': 'multicampus06', 'pwd': 'multicampus06'},
            {'id': 'multicampus07', 'pwd': 'multicampus07'}]

    return JsonResponse(list, safe=False)

def chart (request) :
    context = { 'msg' : [2,3,4,5]}
    return render (request, 'chartDemo.html', context)
