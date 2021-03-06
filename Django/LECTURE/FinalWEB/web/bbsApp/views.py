from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
# select * from table ;
# -> modelName.objects.all()

# select * from table where id = xxxx;
# -> modelName.objects.get(id = xxxx)
# -> modelName.objects.filter(id = xxxx)

# select * from table where id = xxxx and pwd = xxxx ;
# -> modelName.objects.get(id = xxxx, pwd = xxxx)
# -> modelName.objects.filter(id = xxxx, pwd= xxxx)

# select * from table where id = xxxx or pwd = xxxx ;
# -> modelName.objects.filter(Q(id = xxxx) | Q(pwd = xxxx))

# select * from table where subject like '%공지%' ;
# -> modelName.objects.filter(subject_icontains='공지')
# -> modelName.objects.filter(subject_startswith='공지')
# -> modelName.objects.filter(subject_ebdwith='공지')

# insert into table values()
# model(attr=value, attr=value)
# model.save()

# delete * from tableName where id = xxxx
# -> modelName.objects.get(id=xxx).delete()

# update tableName set attr = value where id = xxxx
# obj = modelName.objects.get (id= xxxx)
# obj.attr = value
# obj.save() -- commit

# 사용자의 상태정보 저장을 위해서는 session, cookie

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
        user = BbsUserRegister.objects.get(user_id=id, user_pwd=pwd)
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
        register = BbsUserRegister(user_id=id, user_pwd=pwd, user_name=name)
        register.save()
    return render(request, 'login.html')

# 게시판
def bbs_list(request):
    boards = Bbs.objects.all()
    print('bbs_list request -', type(boards), boards)
    context = {'boards' : boards,
               'name'   : request.session['user_name'],
               'id'   : request.session['user_id']}
    return  render(request, 'list.html', context)

def bbs_registerForm(request):
    print('request bbs_registerForm =')
    context = {'name'   : request.session['user_name'],
               'id'   : request.session['user_id']}
    return  render(request, 'bbsRegisterForm.html', context)

def bbs_register(request):
    title = request.POST ['title']
    content = request.POST['content']
    writer = request.POST['writer']
    print('request bbs_register -', title, content, writer)
    board = Bbs(title = title, content = content, writer = writer)
    board.save()
    return redirect ('bbs_list')


def bbs_read(request, id):
    # select * from bbs where id = id
    # update table set viewcnt = viewcnt +1 value where id = id

    print('request bbs_read -', id)
    board = Bbs.objects.get(id=id)
    board.viewcnt = board.viewcnt + 1
    board.save()
    print('request bbs_read result -', board)
    context = {'board' : board,
               'name': request.session['user_name'],
               'id': request.session['user_id']
               }
    return render(request, 'read.html', context)

def bbs_remove (request):
    id = request.POST['id']
    print('request bbs_remove param -', id)
    # delete from table where id = id
    Bbs.objects.get(id=id).delete()
    return redirect('bbs_list')

def bbs_modifyFrom (request):
    id = request.POST['id']
    board = Bbs.objects.get(id=id)
    context = {'board': board,
               'name': request.session['user_name'],
               'id': request.session['user_id']
               }
    return render (request, 'modify.html', context)

def bbs_modify (request):
    id      = request.POST['id']
    title   = request.POST['title']
    content = request.POST['content']
    writer  = request.POST['writer']
    print('request modify -', id, title, content, writer)
    board   = Bbs.objects.get(id=id)
    board.title = title
    board.content = content
    board.save()
    return redirect('bbs_list')

# update tableName set attr = value where id = xxxx
# obj = modelName.objects.get (id= xxxx)
# obj.attr = value
# obj.save() -- commit


def bbs_search (request):
    type = request.POST['type']
    keyword = request.POST['keyword']
    print('request bbs_search - ', type, keyword)

    if type == 'title' :
        boards = Bbs.objects.filter(title__icontains = keyword)
    if type == 'writer' :
        boards = Bbs.objects.filter(writer__startwith = keyword)
    list = []
    for board in boards:
        list.append({
            'id' : board.id,
            'title' : board.title,
            'writer' : board.writer,
            'regdate' : board.regdate,
            'viewcnt' : board.viewcnt
        })
    return JsonResponse(list, safe=False)

    # select *
    # ary = modelName.objects.filter(subject(title or writer)_startswith='keyword')
    # list = [{}, {}]