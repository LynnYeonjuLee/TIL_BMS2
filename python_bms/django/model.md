## 1. model type

### CharField(max_lenth=None)

- 길이의 제한이 있는 문자열을 넣을 때 사용
- max_length가 필수인자
- 필드의 최대 길이, 데이터베이스와 django의 유효성 검사에서 사용

> ### `CharField`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#charfield)
>
> - *class* `CharField`(*max_length=None*, ***options*)[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField)
>
>   
>
> A string field, for small- to large-sized strings.
>
> For large amounts of text, use [`TextField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.TextField).
>
> The default form widget for this field is a [`TextInput`](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.TextInput).
>
> [`CharField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField) has one extra required argument:
>
> - `CharField.``max_length`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField.max_length)
>
>   The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation using [`MaxLengthValidator`](https://docs.djangoproject.com/en/3.1/ref/validators/#django.core.validators.MaxLengthValidator).





### TextField()

- 글자의 수가 많을 때 사용
- `<textarea>` 태그를 기본값으로 가지고 있음

> ### `TextField`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#textfield)
>
> - *class* `TextField`(***options*)[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.TextField)
>
>   
>
> A large text field. The default form widget for this field is a [`Textarea`](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.Textarea).
>
> If you specify a `max_length` attribute, it will be reflected in the [`Textarea`](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.Textarea) widget of the auto-generated form field. However it is not enforced at the model or database level. Use a [`CharField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.CharField) for that.





### DateTimeField()

- 최초 생성 일자: `auto_now_add=True`
  - django ORM이 최초 입력시에만 현재 날짜와 시간으로 갱신
  - 테이블에 어떤 데이터를 최초로 넣을 때
- 최종 수정 일자: auto_now=True
  - django ORM이 save를 할 때마다 현재 날짜와 시간으로 갱신

- django model field 참고하면 다양한 필드의 타입를 확인 할 수 있다.

 

> ### `DateField`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#datefield)
>
> - *class* `DateField`(*auto_now=False*, *auto_now_add=False*, ***options*)[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField)
>
>   
>
> A date, represented in Python by a `datetime.date` instance. Has a few extra, optional arguments:
>
> - `DateField.``auto_now`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField.auto_now)
>
>   Automatically set the field to now every time the object **is saved**. Useful for “last-modified” timestamps. Note that the current date is *always* used; it’s not just a default value that you can override.The field is only automatically updated when calling [`Model.save()`](https://docs.djangoproject.com/en/3.1/ref/models/instances/#django.db.models.Model.save). The field isn’t updated when making updates to other fields in other ways such as [`QuerySet.update()`](https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.update), though you can specify a custom value for the field in an update like that.
>
> - `DateField.``auto_now_add`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField.auto_now_add)
>
>   Automatically set the field to now when the object is **first created**. Useful for creation of timestamps. Note that the current date is *always* used; it’s not just a default value that you can override. So even if you set a value for this field when creating the object, it will be ignored. If you want to be able to modify this field, set the following instead of `auto_now_add=True`:For [`DateField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField): `default=date.today` - from [`datetime.date.today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today)For [`DateTimeField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateTimeField): `default=timezone.now` - from [`django.utils.timezone.now()`](https://docs.djangoproject.com/en/3.1/ref/utils/#django.utils.timezone.now)
>
> The default form widget for this field is a [`DateInput`](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.DateInput). The admin adds a JavaScript calendar, and a shortcut for “Today”. Includes an additional `invalid_date` error message key.
>
> The options `auto_now_add`, `auto_now`, and `default` are mutually exclusive. Any combination of these options will result in an error.

> ### `DateTimeField`[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#datetimefield)
>
> - *class* `DateTimeField`(*auto_now=False*, *auto_now_add=False*, ***options*)[¶](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateTimeField)
>
>   
>
> A date and time, represented in Python by a `datetime.datetime` instance. Takes the same extra arguments as [`DateField`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.DateField).
>
> The default form widget for this field is a single [`DateTimeInput`](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.DateTimeInput). The admin uses two separate [`TextInput`](https://docs.djangoproject.com/en/3.1/ref/forms/widgets/#django.forms.TextInput) widgets with JavaScript shortcuts.





## 2. migration

### 주요 명령어

- **makemigrations** 
  - model을 변경한 것에 기반한 새로운 마이그레이션(설계도)을 만들 때 사용
  - 모델을 활성화 하기 전에 DB 설계도를 작성
  - 생성된 마이그레이션 파일은 데이터 베이스 스키마를 위한 버전관리 시스템이라고 생각
  - 모델의 변경사항이 생길때 마다 반드시 실행해줘야 한다.
  - git commit과 유사한 매커니즘(변경사항을 기록해 나간다.)



- **migrate** 
  - 작성된 마이그레이션 파일들을 기반으로 실제 DB 에 반영
  - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
  - 반영된 DB를 시각적으로 확인하기위해 `sqlite`확장프로그램 설치
  - 확인하는 방법
    - DB파일 우클릭 후 open database 클릭
    - 좌측 하단에 sqlite explore 생성
    - 테이블을 클릭하면 schema 확인가능
    - 화살표 클릭시 vscode로 table확인



- **sqlmigrate** 
  - 해당 마이그레이션 파일이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인 하기 위한 명령어
  - `python manage.py sqlmigrate articles 0001` 
  - article앱의 0001번 migration 확인



- **showmigrations** : 

  - 프로젝트 전체의 마이그레이션과 각각의 상태를 확인하기 위해 사용
  - 마이그레이션 파일들의 migrate여부를 확인하기 위한 명령어

  ```bash
  articles
   [X] 0001_initial
   [X] 0002_article_updated_at
   # [ X ] 확인이 되었다는 표시
  ```



### Model 의 중요 3단계

1. models.py : 변경사항(작성, 수정, 삭제..) 발생
2. makemigrations : 마이그레이션(설계도) 만들기
3. migrate : DB에 적용



## DB API

#### Manager

- django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
- 기본적으로 모든 django 모델 클래스에 objects라는 Manager를 추가



#### QuerySet

- 데이터베이스로부터 전달받은 객체 목록
- queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
- 데이터베이스로부터 조회, 필터, 정렬 등을 수행 할 수 있음

```python
Article.object.all()
# Article과 all부분만 변경
# 순수한 python문법이 아닌 django manager에서 운용되는 문법
```

