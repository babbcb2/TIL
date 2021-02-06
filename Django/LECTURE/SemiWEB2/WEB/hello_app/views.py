from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def classboard (reqeust):
    return render(reqeust, 'classboard.html')

def list (reqeust):
    boards = Quiz.objects.all()
    print('list request -', type(boards), boards)
    context = {'boards': boards,
               'name' : reqeust.session['user_name'],
               'id' : reqeust.session['user_id']}
    return render(reqeust, 'list.html', context)

def postForm (reqeust):
    print ('request postFrom =')
    context = {'name' : reqeust.session['user_name'],
               'id' : reqeust.session['user_id']}
    return render(reqeust, 'post.html', context)

def post (request):
    title = request.POST['title']
    content = request.POST['content']
    writer = request.POST['writer']
    explanation = request.POST['explanation']
    answer = request.POST['answer']
    classType = request.POST['classType']
    board = Quiz(title=title, content=content, writer=writer,
                 explanation=explanation, answer=answer, classType=classType)
    board.save()
    return redirect('list')

def read (request, id):
    board = Quiz.objects.get(id=id)
    board.save
    print('request result - ', board)
    context = {'board' : board,
               'name': request.session['user_name'],
               'id': request.session['user_id']
               }
    return render(request, 'read.html', context)

def modifyFrom (request):
    id = request.POST['id']
    board = Quiz.objects.get(id=id)
    context = {'board': board,
               'name': request.session['user_name'],
               'id': request.session['user_id']
               }
    return render (request, 'modify.html', context)

def modify (request):
    id = request.POST['id']
    title = request.POST['title']
    content = request.POST['content']
    explanation = request.POST['explanation']
    answer = request.POST['answer']
    print ('request -', title, content, explanation, answer)
    board = Quiz.objects.get(id=id)
    board.title = title
    board.content = content
    board.explanation = explanation
    board.answer = answer
    board.save()
    return redirect('list')

def remove (request):
    id = request.POST['id']
    print('request remove -', id)
    Quiz.objects.get(id=id).delete()
    return redirect('list')

def answerFrom (request):
    id = request.POST['id']
    board = Quiz.objects.get(id=id)
    context = {'board' : board}
    return render (request, 'answer.html', context)

def answer (request):
    id = request.POST['id']
    answer = request.POST['answer']
    print ('request -', answer)
    board = Quiz.objects.get(id=id)
    board.answer = answer
    board.save()
    return redirect('list')

# -------------- login ---------------

def index(request):
    if request.session.get ('user_id') and request.session.get ('user_name'):
        # return  redirect ('login')
        context = {'id':request.session['user_id'],
                   'name':request.session['user_name']}
        return render(request, 'home.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    request.session['user_name']    = {}
    request.session['user_id']      = {}
    request.session.modified        = True
    return redirect('index')

def loginProc (request):
    print('request - loginProc')
    if request.method == 'GET':
        return redirect('index')
    elif request.method == 'POST':
        id = request.POST['id']
        pwd = request.POST['pwd']
        # select * from BbsUserRegister where user_id = id and user_pwd = pwd
        # orm class - table
        user = UserRegister.objects.get(user_id=id, user_pwd=pwd)
        print('user result -', user)
        context = {}
        if user is not None :
            request.session['user_name'] = user.user_name   # session 생성하는 작업
            request.session['user_id'] = user.user_id
            context['name'] = request.session['user_name']  # session 메모리상에 심는작업
            context['id'] = request.session['user_id']
            return render (request, 'home.html', context)
        else :
            return redirect('index')

def join(request):
    print('request - registerForm')
    return render(request, 'join.html')

def register(request):
    # id, pwd, name -> model > db (insert)
    if request.method == 'POST':
        id = request.POST ['id']
        pwd = request.POST['pwd']
        name = request.POST['name']
        register = UserRegister(user_id=id, user_pwd=pwd, user_name=name)
        register.save()
    return render(request, 'login.html')