from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model): # 상속
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 유저 모델을 참조하는 방식 3가지 
    # 1. User (x)
    # 2. get_user_model() => model 제외 모든 부분에서 사용 
    # 3. settings.AUTH_USER_MODEL => model 에서만 사용 

    # from django.conf import settings
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
