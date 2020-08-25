## 0820_Workshop 정리

### 1. 환경설정

1. 프로젝트와 앱을 실행한다. `(terminal에서 실행)`

   ```bash
   $ django-admin startproject (project_name)
   $ cd project name
   $ python manage.py startapp (app_name)
   ```

2. settings.py 설정하기

   ```python
   1. INSTALLED_APPS 에 app을 추가
   2. 모든 app의 templates를 활용할수 있도록 설정
   	TEMPLATES - 'DIRS': [ BASE_DIR / 'pjt_name' / 'templates']
       # 각 app의 templates폴더에 app이름으로 하위폴더를 생성해준다.
   ```

3. templates폴더 생성
   - app-templates-[app_name] 구조로 폴더를 생성한다.
   - app_name 폴더 하위에 html파일을 생성한다.
   
4. url 독립 시키기

   - crud/urls.py 

     ```python
     from django.contrib import admin
     # 1. include를 추가시켜준다.
     from django.urls import path, include
     
     urlpatterns = [
         path('articles/', include('articles.urls')), # 2. 경로를 articles.urls로 연결
         path('admin/', admin.site.urls),
     ]
     ```

   - articles/urls.py

     ```python
     # 1. 모듈을 삽입한다.
     from django.urls import path
     from . import views
     
     # 2. 변수에 앱의 이름을 저장한다.
     app_name = 'articles'
     urlpatterns = [
         path('', views.index, name='index'),  # 3. index path
     ]
     ```

5. template inheritance

   - crud/templates/base.html 생성

     ```html
     # BootstrapCDN 적용이후 body태그안에 다음 코드 삽입
     # (container에 담아놓으면 grid시스템 활용할때 유용하다. /필수 아님)
     
     <div class='container'>
     {% block content %}
     
     {% endblock %}
     </div>
     ```



### 2. 클래스 정의 및 데이터베이스 생성

1. articles/models.py 폴더

   ```python
   from django.db import models
   
   # 아래에 class를 정의한다.(django Model field reference 참고하여 다양한 속성을 정의해보자.)
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   ```

2. migration `(terminal에서 실행)`

   ```bash
   # 1. model을 변경한것에 기반한 새로운 migration(설계도)을 만든다.
   $ python manage.py makemigrations 
   
   # 2. 작성된 migration 파일들을 기반으로 실제 DB에 반영
   $ python manage.py migrate
   ```



### 3. web 만들기

---

![주석 2020-08-21 002749](0820_Workshop.assets/주석 2020-08-21 002749.jpg)

---

> **기본적인 작성순서 **
>
> 1. urls.py 에서 path(경로) 설정
> 2. views.py 에서 함수 정의(중간 관리자)
> 3. template폴더에서 html파일 생성(web화면을 보여주기)
> 4. 위의 구조를 참고하자!

---



#### (1) crud/articles/urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    
    # 1. path경로설정 (name설정을 통해 {{ app_name:name }}문법으로 접근가능)
    #   views에 있는 함수에 접근하도록 유도
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    
    
    # 2. url경로에 <int:~~~>,<str:~~~> 문법을 통해 variable routing이 가능해진다.
    #    아래 url의 경우 각 데이터베이스에 접근시 index역할이 필요하기 때문에 사용.
    path('<int:article_pk>/', views.detail, name="detail"),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/edit/', views.edit, name='edit'),
    path('<int:article_pk>/update/', views.update, name='update'),
]
```



#### (2) crud/articles/views.py

```word
템플릿을 불러오는 !! render !!

context로 원하는 인자를, 즉 view에서 사용하던 python변수를 html템플릿으로 넘길 수 있다.

딕셔너리형으로 사용하며 key값이 변수이름, value값이 변수

render(request, template_name, context=None, content_type=None, status=None, using=None)
```

```word
url로 이동하는 !! redirect !! 
(url에 맞는 view가 다시 실행되며 함수에서 render/redirect결정)

to에는 어느 url로 이동할지를 정한다.(상대,절대 가능), context값을 전달하지는 못함!!!!

redirect(to, permanent=False, *args, **kwargs)
```

```python
# redirect 함수 가져오고, 같은 앱에있는 Article클래스를 사용할 준비를 한다.
from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    # DB에 있는 모든 인스턴스 가져오기(최근에 작성한 문서를 위에서부터 보여주고 싶을 때 [::-1]을 사용)
    articles = Article.objects.all()[::-1]
    # context에 넣음으로서 html파일에서 활용할 수 있다.
    context = {
        'articles' : articles,
    }
    # 'articles/index.html'파일에서 articles변수에 저장된 값을 사용할 수 있도록 해준다.
    return render(request, 'articles/index.html', context)


# 함수 간 간격은 반드시 2줄!!2줄!!띄우기띄우기
def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # form태그에서 받아온 정보를 각각 변수에 저장(POST method활용)
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 클래스 선언후 속성값을 데이터베이스에 저장
    article = Article()
    article.title = title
    article.content = content
    article.save()
    # detail url실행 (article.pk 를 통해 생성한 data를 찾아갈 수 있다.)
    return redirect('articles:detail', article.pk)


def detail(request, article_pk):
    # path를 통해 요청과 article_pk(primary key)값을 전달받음
    # 전달받은 article_pk 에 해당하는 data를 DB에서 꺼내와 변수에 저장
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')


def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.get(pk=article_pk)
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', article_pk)
```



#### (3) templates (index/ new/ detail/ edit)

```html
# templates inheritance(템플릿 상속)
{% extends 'base.html' %}

{% block content %}
<div class="row"></div>
    <h1>INDEX</h1>
	
	# a태그생성 - 클릭시 new.html로 이동 ( 문법주의 )
    <a href="{% url 'articles:new' %}" class="d-flex mb-4">NEW</a>
	
	# views.index에서 context와 render를 통해 보내온 인자(articles)를 활용하는 모습
    {% for article in articles %}
      <h2>제목: {{ article.title }} </h2>
      <p>내용: {{ article.content }} </p>
      <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
      <hr>
    {% endfor %}

{% endblock  %}
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
   
	# method GET은 주로 '조회'를 할 때 사용한다.(Idempotent하게 설계되었음)
	# method POST은 동일한 요청을 전송해도 응답이 다를수 있음(Non-idempotent)->생성에 적합
  <form action="{% url 'articles:create' %}" method="POST">
      
      # 입력값 숨기기
      {% csrf_token %}
      
    TITLE: <input type="text" name="title">
    <br>
    CONTENT: <textarea name="content" id="" cols="30" rows="10">
    </textarea>
    <br>
    <button>작성</button>
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>

{% endblock %}
```

```html
{% extends 'base.html' %}

{% block content %}
<h1>DETAIL</h1>
<hr>
<h2>{{ article.title }}</h2>
<p>{{ article.content }}</p>
<p>작성일: {{ article.created_at|date:"Y년 n월 j일 P" }}</p>
<p>수정일: {{ article.updated_at|date:"Y년 n월 j일 P" }}</p>
<a href="{% url 'articles:edit' article.pk %}">EDIT</a>
<a href="{% url 'articles:delete' article.pk %}">DELETE</a>
<br>
<a href="{% url 'articles:index'%}">BACK</a>
{% endblock  %}
```

```html
{% extends 'base.html' %}

{% block content %}
  <h1>EDIT</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    TITLE: <input type="text" name="title" value="{{ article.title }}">
    <br>
    CONTENT: <textarea name="content" id="" cols="30" rows="10">
    {{ article.content }}
    </textarea>
    <br>
    <button>작성</button>
  </form>
  <a href="{% url 'articles:index' %}">BACK</a>

{% endblock  %}
```



### 결과

![주석 2020-08-21 013951](0820_Workshop.assets/주석 2020-08-21 013951.jpg)

![주석 2020-08-21 014048](0820_Workshop.assets/주석 2020-08-21 014048-1597942025874.jpg)

![주석 2020-08-21 014048](0820_Workshop.assets/주석 2020-08-21 014048-1597941961140.jpg)

![주석 2020-08-21 014203](0820_Workshop.assets/주석 2020-08-21 014203-1597942036424.jpg)

![주석 2020-08-21 014240](0820_Workshop.assets/주석 2020-08-21 014240.jpg)

![주석 2020-08-21 014251](0820_Workshop.assets/주석 2020-08-21 014251.jpg)







