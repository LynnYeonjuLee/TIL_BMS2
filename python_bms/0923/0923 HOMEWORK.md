# 0923 HOMEWORK

## 1. 

1) T 

2) F 

3) T

4) F - 유일해야하지만 pk 일 필요는 없다. 

## 2.

- articles_question
- articles_comment
- answer_id(외래키)

## 3. 

question:comment = 1:N

- question.comment_set.all()



## 4. 

> 로그인을 안한 상황 

1. 로그인 페이지로 이동 
2. 로그인 폼 작성 후 다시 요청(?next= 의 뒤 부분으로 ) delete  함수로  GET 요청 
3. @ require_POST 데코레이터 때문에 에러 발생 
   - 405 Method Not Allowed 

### 해결방법

1. @require_POST 데코레이터 제거 
2. 함수 안에서 if 문으로 해결 



