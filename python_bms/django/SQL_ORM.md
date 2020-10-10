[TOC]

---



## 문제

> 아래의 문제들을 보면서 서로 대응되는 ORM문과 SQL문을 작성하시오.
>
> **python manage.py shell_plus --print-sql**
>
> 위 명령어로 shell_plus 로 sql 문을 같이 확인해보세요.





### 1. 기본 CRUD 로직

1. 모든 user 레코드 조회

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. user 레코드 생성

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

   * 하나의 레코드를 빼고 작성 후 `NOT NULL` constraint 오류를 orm과 sql에서 모두 확인 해보세요.

3. 해당 user 레코드 조회

   - `101` 번 id의 전체 레코드 조회

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

4. 해당 user 레코드 수정

   - ORM: `101` 번 글의 `last_name` 을 '김' 으로 수정
   
```python
   # orm
   ```
   
   ```sql
   -- sql
      ```
   
5. 해당 user 레코드 삭제

   - ORM: `101` 번 글 삭제
   
```python
   # orm
   ```
   
```sql
   -- sql
   ```



---



### 2. 조건에 따른 쿼리문

1. 전체 인원 수 

   - `User` 의 전체 인원수

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

2. 나이가 30인 사람의 이름

   - `ORM` : `.values` 활용
     - 예시: `User.objects.filter(조건).values(컬럼이름)`

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 나이가 30살 이상인 사람의 인원 수

   -  ORM: `__gte` , `__lte` , `__gt`, `__lt` -> 대소관계 활용

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

4. 나이가 20살 이하인 사람의 인원 수 

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

5. 나이가 30이면서 성이 김씨인 사람의 인원 수

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

6. 나이가 30이거나 성이 김씨인 사람?

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

7. 지역번호가 02인 사람의 인원 수

   - `ORM`: `__startswith` 

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

8. 거주 지역이 강원도이면서 성이 황씨인 사람의 이름

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```



---



### 3. 정렬 및 LIMIT, OFFSET

1. 나이가 많은 사람순으로 10명

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 잔액이 적은 사람순으로 10명

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 잔고는 오름차순, 나이는 내림차순으로 10명?

      ```python
   # orm
   ```

   ```sql
   -- sql
   ```
   
4. 성, 이름 내림차순 순으로 5번째 있는 사람

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```



---



### 4. 표현식

> ORM: `aggregate` 사용
>
> https://docs.djangoproject.com/en/2.2/topics/db/aggregation/#aggregation
>
> - '종합', '합계' 등의 사전적 의미
> - 특정 필드 전체의 합, 평균 등을 계산할 때 사용

1. 전체 평균 나이

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

2. 김씨의 평균 나이

      ```python
   # orm
   ```

      ```sql
   -- sql
      ```

3. 강원도에 사는 사람의 평균 계좌 잔고

   ```python
   # orm
   ```

   ```sql
   -- sql
   ```

4. 계좌 잔액 중 가장 높은 값

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```

5. 계좌 잔액 총액

   ```python
   # orm
   ```

      ```sql
   -- sql
      ```