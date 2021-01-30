



Web

FULL STACK

<----- CLIENT SID ----->   FRONT END

- BROWSER( .HTML / .JSP / .ASP)
- HTML  - TAG + TEXT -> 정적파일
- HTML(구조), CSS(표현), SCRIPT(동작)
- 동적코더삽입 (JSP, ASP)



<------- SERVER SIDE ------>   BACK END

- PYTHON
- FRAMEWORK - FLASK, DJANGO
- MVT FRAMEWORK ( M: Model , V : View, T : Template )
- 



> django-admin startproject djangoWEB
>
> dir/w
>
> cd baseWEB
>
> dir/w



{{}} -- print

{% %} -- code (if, for, path)



* static 위치를 지정해는 작업
* 각각의 app에 흩어져있는 static file 을 한 곳으로 모으는 작업

web> python manage.py collectstatic

서버실행 명령어 

python manage.py runserver



클라이언트 브라우저 실행

http://127.0.0.1:8000



manage.py 파일이 있는 디렉토리에서

#### 앱 (App)

> python manage.py	startapp GreetingApp



​									http:// host:port / app / view 함수( urls )

browser (xxx.html) ---------------------------------------------------------> view.py ---> model

​																												:

​								<------------------------------------------------------  templates -> xxx.html

url : xxx. com ?key== value&key   ---> GET 방식

​						 <-- querysting  --> 

url : xxx.com  --> POST  (현장에서는 post 방식을 지향)

-- from (action='destination' method='post|get')



* json (restful service)  -  json([ { key : value } ])

  

* ajax(비동기 통신)

* script -> jquery

* bootstrap (theme)



* orm을 통한 데이터베이스 관리를 위한 계정 생성및 접근

* model 생성 후 admin 등록

  

  model - class >  admin  정리

  > python manage.py createsuperuser
  >
  > python manage.py makemigrations
  >
  > python manage.py migrate



urls --> views

- HttpResponse() - x
- JsonResponse() - json
- render () - templates(xxx.html)
- redirect(path X , alias O)  요청을 재지정



Ajax는 웹 페이지의 디자인 요소와 정보 요소를 분리한다. 

처음 사이트에 접속하면 웹 서버는 해당 페이지의 스타일과 레이아웃을 정의하는 정적 HTML 파일과 CSS 파일, 

그리고 데이터를 어떻게 요청하면 되는지를 설명한 JavaScript 파일을 전달한다. 



브라우저는 일단 이 내용으로 페이지의 기본적인 골격을 구축해 놓는다. 

그리고 골격의 구축이 끝나면 브라우저는 전달받은 JavaScript를 실행해서 서버에 데이터만을 별도로 요청한다.

 이 때 서버에서 주는 응답은 순수한 데이터 객체 즉 XML 또는 JSON 데이터이다.[1] 브라우저가 이 데이터를 수신하면 미리 만들어 둔 틀 안에 적절한 방법으로 데이터를 끼워 넣는다.